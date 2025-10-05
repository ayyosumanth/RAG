# Create rag_pipeline.py - Fixed version
rag_pipeline_py = """import os
from typing import List, Dict, Any, Optional
from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage, SystemMessage, BaseMessage
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
import config
import pandas as pd
from vector_store import MSMEVectorStore
from news_fetcher import NewsAggregator

class MSMERAGPipeline:
    def __init__(self):
        if not config.OPENAI_API_KEY:
            raise ValueError("OpenAI API key not found. Please add OPENAI_API_KEY to your .env file")
            
        self.llm = ChatOpenAI(
            model="gpt-3.5-turbo",
            temperature=0.7,
            openai_api_key=config.OPENAI_API_KEY,
            streaming=True,
            callbacks=[StreamingStdOutCallbackHandler()]
        )
        
        self.vector_store = MSMEVectorStore()
        self.news_aggregator = NewsAggregator()
        self.conversation_history = []
        
    def initialize_knowledge_base(self, companies_file: str, financial_file: str):
        print("Initializing knowledge base...")
        self.vector_store.load_company_data(companies_file, financial_file)
        
        try:
            print("Fetching recent news...")
            recent_news = self.news_aggregator.fetch_all_news(limit=30)
            if recent_news:
                self.vector_store.add_news_articles(recent_news)
                print(f"Added {len(recent_news)} news articles")
            else:
                print("No news articles fetched (API keys may be missing)")
        except Exception as e:
            print(f"Warning: Could not fetch news - {str(e)}")
        
        print("Knowledge base initialized!")
        
    def process_query(self, user_query: str, include_news: bool = True) -> str:
        query_analysis = self._analyze_query(user_query)
        context_docs = self._retrieve_context(user_query, query_analysis)
        
        news_context = []
        if include_news and self._should_include_news(query_analysis):
            news_context = self._get_relevant_news(query_analysis)
        
        full_context = self._build_context(context_docs, news_context)
        response = self._generate_response(user_query, full_context, query_analysis)
        self._update_conversation_history(user_query, response)
        
        return response
    
    def _analyze_query(self, query: str) -> Dict[str, Any]:
        query_lower = query.lower()
        
        analysis = {
            "query_type": "general",
            "sectors": [],
            "companies": [],
            "metrics": [],
            "time_focus": "current",
            "needs_news": False,
            "needs_financial": False,
            "needs_comparison": False
        }
        
        if any(word in query_lower for word in ["compare", "comparison", "vs", "versus", "against"]):
            analysis["query_type"] = "comparison"
            analysis["needs_comparison"] = True
        elif any(word in query_lower for word in ["trend", "trends", "growth", "performance"]):
            analysis["query_type"] = "trend_analysis"
            analysis["needs_financial"] = True
        elif any(word in query_lower for word in ["news", "latest", "recent", "updates"]):
            analysis["query_type"] = "news_inquiry"
            analysis["needs_news"] = True
        elif any(word in query_lower for word in ["financial", "revenue", "profit", "assets"]):
            analysis["query_type"] = "financial_analysis"
            analysis["needs_financial"] = True
        
        for sector, keywords in config.SECTOR_KEYWORDS.items():
            if sector.lower() in query_lower or any(keyword in query_lower for keyword in keywords):
                analysis["sectors"].append(sector)
        
        financial_terms = ["revenue", "profit", "margin", "assets", "ratio", "growth", "performance"]
        analysis["metrics"] = [term for term in financial_terms if term in query_lower]
        
        if any(word in query_lower for word in ["news", "latest", "recent", "market", "trends"]):
            analysis["needs_news"] = True
            
        return analysis
    
    def _retrieve_context(self, query: str, analysis: Dict[str, Any]) -> List[Dict]:
        context_docs = []
        
        base_results = self.vector_store.search_similar(query, n_results=8)
        context_docs.extend(base_results)
        
        for sector in analysis["sectors"]:
            sector_results = self.vector_store.search_by_sector(query, sector, n_results=5)
            context_docs.extend(sector_results)
        
        if analysis["needs_financial"] or analysis["query_type"] == "financial_analysis":
            financial_results = self.vector_store.search_similar(
                f"{query} financial performance metrics",
                n_results=5,
                filter_dict={"type": "company"}
            )
            context_docs.extend(financial_results)
        
        seen_ids = set()
        unique_docs = []
        for doc in context_docs:
            if doc["id"] not in seen_ids:
                seen_ids.add(doc["id"])
                unique_docs.append(doc)
        
        return unique_docs[:15]
    
    def _should_include_news(self, analysis: Dict[str, Any]) -> bool:
        return (analysis["needs_news"] or 
                analysis["query_type"] in ["news_inquiry", "trend_analysis"] or
                any(keyword in analysis.get("sectors", []) for keyword in config.SECTOR_KEYWORDS.keys()))
    
    def _get_relevant_news(self, analysis: Dict[str, Any]) -> List[Dict]:
        news_articles = []
        
        for sector in analysis["sectors"]:
            try:
                sector_news = self.news_aggregator.fetch_sector_news(sector, limit=5)
                news_articles.extend(sector_news)
            except Exception as e:
                print(f"Could not fetch news for {sector}: {str(e)}")
        
        if not analysis["sectors"]:
            try:
                general_news = self.news_aggregator.fetch_all_news(limit=8)
                news_articles.extend(general_news)
            except Exception as e:
                print(f"Could not fetch general news: {str(e)}")
        
        return news_articles[:10]
    
    def _build_context(self, context_docs: List[Dict], news_context: List[Dict]) -> str:
        context_parts = []
        
        if context_docs:
            context_parts.append("=== COMPANY AND FINANCIAL DATA ===")
            for doc in context_docs[:10]:
                metadata = doc["metadata"]
                doc_type = metadata.get("type", "unknown")
                
                if doc_type == "company":
                    context_parts.append(f"• {metadata.get('company_name', 'Unknown Company')} ({metadata.get('sector', 'Unknown Sector')}):")
                    context_parts.append(f"  {doc['document'][:500]}...")
                else:
                    context_parts.append(f"• {doc['document'][:300]}...")
        
        if news_context:
            context_parts.append("\\n=== RECENT NEWS AND MARKET UPDATES ===")
            for article in news_context[:8]:
                context_parts.append(f"• [{article.get('source', 'Unknown Source')}] {article.get('title', 'No Title')}")
                if article.get('description'):
                    context_parts.append(f"  {article['description'][:200]}...")
                if article.get('sentiment'):
                    context_parts.append(f"  Sentiment: {article['sentiment']}")
        
        return "\\n".join(context_parts)
    
    def _generate_response(self, query: str, context: str, analysis: Dict[str, Any]) -> str:
        system_prompt = self._build_system_prompt(analysis)
        
        user_prompt = f\"\"\"Based on the following context about MSME companies, financial data, and market news, please answer the user's question comprehensively.

CONTEXT:
{context}

USER QUESTION: {query}

Please provide a detailed, accurate response that:
1. Directly answers the user's question
2. Uses specific data and examples from the context
3. Provides actionable insights where relevant
4. Mentions sources when citing specific information
5. Highlights any important trends or patterns

Response:\"\"\"
        
        messages = [
            SystemMessage(content=system_prompt),
            HumanMessage(content=user_prompt)
        ]
        
        if self.conversation_history:
            recent_history = self.conversation_history[-4:]
            history_text = "\\n".join([f"User: {h['user']}\\nAssistant: {h['assistant'][:200]}..." 
                                     for h in recent_history])
            messages.insert(1, HumanMessage(content=f"Previous conversation context:\\n{history_text}"))
        
        try:
            response = self.llm(messages)
            return response.content
        except Exception as e:
            return f"I apologize, but I encountered an error while processing your request: {str(e)}. Please try rephrasing your question."
    
    def _build_system_prompt(self, analysis: Dict[str, Any]) -> str:
        base_prompt = \"\"\"You are an expert MSME (Micro, Small, and Medium Enterprise) market intelligence analyst with deep knowledge of Indian business markets, financial analysis, and industry trends. You specialize in providing actionable insights for MSME companies across Manufacturing, Food Processing, Technology, Healthcare, and Textiles sectors.\"\"\"
        
        if analysis["query_type"] == "financial_analysis":
            return base_prompt + " Focus on financial metrics, ratios, performance analysis, and provide specific numerical insights. Compare companies when relevant and highlight growth patterns."
        
        elif analysis["query_type"] == "news_inquiry":
            return base_prompt + " Focus on recent market developments, news analysis, and their implications for MSME companies. Provide timely insights and trend analysis."
        
        elif analysis["query_type"] == "comparison":
            return base_prompt + " Provide detailed comparative analysis between companies, sectors, or metrics. Use tables or structured comparisons when helpful."
        
        elif analysis["query_type"] == "trend_analysis":
            return base_prompt + " Focus on identifying patterns, trends, and market movements. Provide forward-looking insights and strategic recommendations."
        
        else:
            return base_prompt + " Provide comprehensive, well-structured responses that combine company data, financial insights, and market intelligence."
    
    def _update_conversation_history(self, user_query: str, response: str):
        self.conversation_history.append({
            "user": user_query,
            "assistant": response,
            "timestamp": str(pd.Timestamp.now())
        })
        
        if len(self.conversation_history) > 10:
            self.conversation_history = self.conversation_history[-10:]
    
    def get_sector_summary(self, sector: str) -> str:
        query = f"Provide a comprehensive overview of {sector} sector companies, their performance, and market trends"
        return self.process_query(query, include_news=True)
    
    def get_company_analysis(self, company_name: str) -> str:
        query = f"Provide detailed analysis of {company_name} including financial performance, market position, and recent developments"
        return self.process_query(query, include_news=True)
    
    def clear_history(self):
        self.conversation_history = []

if __name__ == "__main__":
    try:
        rag = MSMERAGPipeline()
        print("RAG Pipeline created successfully!")
    except Exception as e:
        print(f"Error creating RAG pipeline: {str(e)}")
        print("Make sure you have OPENAI_API_KEY in your .env file")
"""

with open('rag_pipeline.py', 'w') as f:
    f.write(rag_pipeline_py)

print("rag_pipeline.py created!")