# Create vector_store.py - ChromaDB implementation
vector_store_py = '''import chromadb
import pandas as pd
import numpy as np
from typing import List, Dict, Any
import json
from datetime import datetime
import config
import uuid

class MSMEVectorStore:
    """
    ChromaDB vector store for MSME companies, financial data, and news
    """
    
    def __init__(self):
        self.client = chromadb.PersistentClient(path=config.CHROMA_PERSIST_DIRECTORY)
        self.collection = self.client.get_or_create_collection(
            name=config.COLLECTION_NAME,
            metadata={"hnsw:space": "cosine"}
        )
        
    def load_company_data(self, companies_file: str, financial_file: str):
        """Load MSME company and financial data into vector store"""
        # Load datasets
        companies_df = pd.read_csv(companies_file)
        financial_df = pd.read_csv(financial_file)
        
        # Prepare documents for embedding
        documents = []
        metadatas = []
        ids = []
        
        print(f"Loading {len(companies_df)} companies into vector store...")
        
        for _, company in companies_df.iterrows():
            company_id = company['Company_ID']
            
            # Get financial data for this company
            company_financials = financial_df[financial_df['Company_ID'] == company_id]
            
            # Create comprehensive document text
            doc_text = self._create_company_document(company, company_financials)
            
            # Create metadata
            metadata = {
                "type": "company",
                "company_id": company_id,
                "company_name": company['Company_Name'],
                "sector": company['Sector'],
                "location": company['Location'],
                "founded_year": int(company['Founded_Year']),
                "employee_count": int(company['Employee_Count']),
                "credit_rating": str(company.get('Credit_Rating', 'N/A')),
                "risk_level": str(company.get('Risk_Level', 'N/A')),
                "market_outlook": str(company.get('Market_Outlook', 'N/A'))
            }
            
            documents.append(doc_text)
            metadatas.append(metadata)
            ids.append(f"company_{company_id}")
        
        # Add to collection
        self.collection.add(
            documents=documents,
            metadatas=metadatas,
            ids=ids
        )
        
        print(f"Successfully loaded {len(documents)} company records!")
    
    def add_news_articles(self, articles: List[Dict[str, Any]]):
        """Add news articles to the vector store"""
        if not articles:
            return
            
        documents = []
        metadatas = []
        ids = []
        
        print(f"Adding {len(articles)} news articles to vector store...")
        
        for article in articles:
            # Create document text from article
            doc_text = self._create_news_document(article)
            
            # Create metadata
            metadata = {
                "type": "news",
                "source": article.get("source", ""),
                "title": article.get("title", "")[:100],  # Truncate long titles
                "category": article.get("category", "business"),
                "published_at": article.get("published_at", ""),
                "url": article.get("url", ""),
                "source_name": article.get("source_name", "")
            }
            
            # Add sentiment if available
            if "sentiment" in article:
                metadata["sentiment"] = article["sentiment"]
                metadata["sentiment_score"] = float(article.get("sentiment_score", 0.0))
            
            documents.append(doc_text)
            metadatas.append(metadata)
            ids.append(f"news_{uuid.uuid4().hex}")
        
        # Add to collection
        self.collection.add(
            documents=documents,
            metadatas=metadatas,
            ids=ids
        )
        
        print(f"Successfully added {len(documents)} news articles!")
    
    def search_similar(self, query: str, n_results: int = 10, filter_dict: Dict = None) -> List[Dict]:
        """Search for similar content in the vector store"""
        
        # Prepare where clause for filtering
        where_clause = {}
        if filter_dict:
            where_clause.update(filter_dict)
        
        # Perform search
        results = self.collection.query(
            query_texts=[query],
            n_results=n_results,
            where=where_clause if where_clause else None
        )
        
        # Format results
        formatted_results = []
        if results["documents"] and results["documents"][0]:
            for i in range(len(results["documents"][0])):
                formatted_results.append({
                    "document": results["documents"][0][i],
                    "metadata": results["metadatas"][0][i],
                    "distance": results["distances"][0][i] if results.get("distances") else None,
                    "id": results["ids"][0][i]
                })
        
        return formatted_results
    
    def search_by_sector(self, query: str, sector: str, n_results: int = 5) -> List[Dict]:
        """Search for content related to a specific sector"""
        return self.search_similar(
            query=query,
            n_results=n_results,
            filter_dict={"sector": sector}
        )
    
    def search_companies_by_criteria(self, sector: str = None, risk_level: str = None, 
                                   min_employees: int = None) -> List[Dict]:
        """Search companies by specific criteria"""
        where_clause = {"type": "company"}
        
        if sector:
            where_clause["sector"] = sector
        if risk_level:
            where_clause["risk_level"] = risk_level
        if min_employees:
            where_clause["employee_count"] = {"$gte": min_employees}
        
        results = self.collection.query(
            query_texts=["company information"],
            n_results=50,
            where=where_clause
        )
        
        return results
    
    def get_recent_news(self, hours: int = 24, category: str = None) -> List[Dict]:
        """Get recent news articles"""
        where_clause = {"type": "news"}
        if category:
            where_clause["category"] = category
        
        results = self.collection.query(
            query_texts=["latest news updates"],
            n_results=20,
            where=where_clause
        )
        
        return results
    
    def _create_company_document(self, company: pd.Series, financials: pd.DataFrame) -> str:
        """Create a comprehensive text document for a company"""
        
        # Basic company info
        doc_parts = [
            f"Company: {company['Company_Name']}",
            f"Sector: {company['Sector']}",
            f"Location: {company['Location']}",
            f"Founded: {company['Founded_Year']}",
            f"Employees: {company['Employee_Count']}",
            f"Primary Products: {company['Primary_Products']}",
            f"Certifications: {company.get('Certifications', 'N/A')}",
            f"Export Markets: {company.get('Export_Markets', 'N/A')}",
            f"Credit Rating: {company.get('Credit_Rating', 'N/A')}",
            f"Risk Level: {company.get('Risk_Level', 'N/A')}",
            f"Market Outlook: {company.get('Market_Outlook', 'N/A')}"
        ]
        
        # Add financial information if available
        if not financials.empty:
            latest_year = financials['Year'].max()
            latest_financials = financials[financials['Year'] == latest_year].iloc[0]
            
            doc_parts.extend([
                f"Latest Revenue ({latest_year}): ₹{latest_financials['Revenue_Crores']:.2f} crores",
                f"Net Profit ({latest_year}): ₹{latest_financials['Net_Profit_Crores']:.2f} crores",
                f"Profit Margin: {latest_financials['Profit_Margin_Percent']:.2f}%",
                f"Total Assets: ₹{latest_financials['Total_Assets_Crores']:.2f} crores",
                f"Debt-to-Equity Ratio: {latest_financials['Debt_to_Equity_Ratio']:.2f}",
                f"Current Ratio: {latest_financials['Current_Ratio']:.2f}",
                f"Return on Assets: {latest_financials['ROA_Percent']:.2f}%"
            ])
            
            # Add growth trends if multiple years available
            if len(financials) > 1:
                revenue_growth = ((latest_financials['Revenue_Crores'] - 
                                financials.iloc[0]['Revenue_Crores']) / 
                                financials.iloc[0]['Revenue_Crores'] * 100)
                doc_parts.append(f"Revenue Growth: {revenue_growth:.2f}%")
        
        # Add other relevant information
        if pd.notna(company.get('Growth_Drivers')):
            doc_parts.append(f"Growth Drivers: {company['Growth_Drivers']}")
        
        if pd.notna(company.get('Key_Challenges')):
            doc_parts.append(f"Key Challenges: {company['Key_Challenges']}")
        
        if pd.notna(company.get('Digital_Maturity_Level')):
            doc_parts.append(f"Digital Maturity: {company['Digital_Maturity_Level']}")
        
        return " | ".join(doc_parts)
    
    def _create_news_document(self, article: Dict[str, Any]) -> str:
        """Create a text document from news article"""
        doc_parts = [
            f"Title: {article.get('title', '')}",
            f"Source: {article.get('source_name', article.get('source', ''))}",
            f"Category: {article.get('category', 'business')}"
        ]
        
        if article.get('description'):
            doc_parts.append(f"Description: {article['description']}")
        
        if article.get('content'):
            doc_parts.append(f"Content: {article['content']}")
        
        if article.get('published_at'):
            doc_parts.append(f"Published: {article['published_at']}")
        
        if article.get('sentiment'):
            doc_parts.append(f"Sentiment: {article['sentiment']} (Score: {article.get('sentiment_score', 0)})")
        
        return " | ".join(doc_parts)
    
    def get_collection_stats(self) -> Dict[str, Any]:
        """Get statistics about the vector store collection"""
        try:
            collection_count = self.collection.count()
            
            # Get sample of documents to analyze types
            sample = self.collection.query(
                query_texts=["sample"],
                n_results=min(100, collection_count)
            )
            
            types_count = {}
            if sample["metadatas"] and sample["metadatas"][0]:
                for metadata in sample["metadatas"][0]:
                    doc_type = metadata.get("type", "unknown")
                    types_count[doc_type] = types_count.get(doc_type, 0) + 1
            
            return {
                "total_documents": collection_count,
                "document_types": types_count,
                "collection_name": config.COLLECTION_NAME
            }
        except Exception as e:
            return {"error": str(e)}

# Test the vector store
if __name__ == "__main__":
    store = MSMEVectorStore()
    print("Vector store created successfully!")
    print("Stats:", store.get_collection_stats())
'''

with open('vector_store.py', 'w') as f:
    f.write(vector_store_py)

print("vector_store.py created!")