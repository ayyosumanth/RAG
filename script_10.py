# Create comprehensive README.md
readme_md = """# MSME News Aggregator & Market Intelligence RAG Chatbot

A sophisticated RAG (Retrieval-Augmented Generation) chatbot built for MSME (Micro, Small, and Medium Enterprises) market intelligence. This system combines your company dataset with real-time news from multiple APIs to provide comprehensive market insights and business intelligence.

## 🚀 Features

### 🤖 **Intelligent RAG Chatbot**
- **Natural Language Queries**: Ask questions about companies, sectors, financial performance
- **Context-Aware Responses**: Maintains conversation history for follow-up questions
- **Multi-Source Intelligence**: Combines company data + financial metrics + real-time news

### 📰 **Multi-API News Integration**
- **NewsData.io**: Indian business news with sector filtering
- **Finnhub**: Financial market news and updates
- **Alpha Vantage**: News with sentiment analysis
- **MarketAux**: Global market news and trends

### 📊 **Advanced Analytics Dashboard**
- **Performance Metrics**: Real-time KPIs and sector comparisons
- **Interactive Charts**: Revenue trends, growth analysis, risk assessment
- **Sector Intelligence**: Deep-dive analytics by industry vertical

### 🗄️ **Vector Database (ChromaDB)**
- **Semantic Search**: Find relevant companies and news by meaning, not just keywords
- **Persistent Storage**: Maintains knowledge base across sessions
- **Real-time Updates**: Automatically indexes new news articles

## 📋 **Your Dataset Integration**

The system automatically loads and processes your MSME datasets:

### **Company Dataset** (`NewCompanyDATAset.csv`)
- ✅ **50 companies** across 5 sectors (Manufacturing, Food Processing, Technology, Healthcare, Textiles)
- ✅ **Comprehensive profiles**: Contact info, certifications, market position
- ✅ **Performance scores**: Financial, operational, innovation metrics
- ✅ **Risk assessment**: Credit ratings and risk levels

### **Financial Dataset** (`msme_financial_data.csv`)  
- ✅ **3-year financial data** (2022-2024) for all companies
- ✅ **Key metrics**: Revenue, profit margins, asset ratios, ROA
- ✅ **Growth tracking**: Year-over-year performance analysis

## 🛠️ **Quick Start Guide**

### **Step 1: Install Dependencies**
```bash
pip install -r requirements.txt
```

### **Step 2: Configure API Keys**
1. Copy `.env.example` to `.env`
2. Add your API keys (at minimum, you need OpenAI):

```env
OPENAI_API_KEY=your_openai_api_key_here
NEWSDATA_API_KEY=your_newsdata_api_key_here  # Optional but recommended
FINNHUB_API_KEY=your_finnhub_api_key_here    # Optional
ALPHA_VANTAGE_API_KEY=your_alpha_vantage_key # Optional  
MARKETAUX_API_KEY=your_marketaux_api_key     # Optional
```

### **Step 3: Run the Application**
```bash
streamlit run app.py
```

### **Step 4: Initialize the System**
1. Open the app in your browser (usually `http://localhost:8501`)
2. Enter your API keys in the sidebar
3. Click "🚀 Initialize System" 
4. Wait for successful initialization
5. Start chatting with your MSME data!

## 🔑 **API Keys Guide**

### **Required APIs**
| API | Purpose | Get Key From | Cost |
|-----|---------|--------------|------|
| **OpenAI** | AI Responses | [OpenAI Platform](https://platform.openai.com/api-keys) | Pay-per-use |

### **Optional News APIs** (Enhance market intelligence)
| API | Purpose | Get Key From | Free Tier |
|-----|---------|--------------|-----------|
| **NewsData.io** | Indian Business News | [NewsData.io](https://newsdata.io/) | 200 requests/day |
| **Finnhub** | Financial Market News | [Finnhub](https://finnhub.io/) | 60 calls/minute |
| **Alpha Vantage** | News + Sentiment | [Alpha Vantage](https://www.alphavantage.co/) | 5 calls/minute |
| **MarketAux** | Market News | [MarketAux](https://www.marketaux.com/) | 100 requests/day |

## 💬 **Example Queries**

### **Company Analysis**
- "Tell me about Oilmax Systems' financial performance"
- "Compare healthcare companies in my dataset"
- "Which manufacturing companies have the highest growth rates?"

### **Sector Intelligence**  
- "What are the latest trends in the technology sector?"
- "Show me food processing companies with strong export potential"
- "Analyze the risk levels across textile companies"

### **Market Insights**
- "What recent news affects the manufacturing sector?"
- "Give me a comprehensive overview of healthcare MSMEs"
- "Which sectors show the best investment potential?"

### **Financial Analysis**
- "Show companies with profit margins above 20%"
- "Identify high-growth companies in my portfolio"
- "Compare debt-to-equity ratios across sectors"

## 🏗️ **System Architecture**

```
📱 Streamlit UI
    ↓
🧠 RAG Pipeline (LangChain + OpenAI)
    ↓
🗄️ ChromaDB Vector Store ← 📰 Multi-API News Fetcher
    ↓                          ↓
📊 Your MSME Data         🌐 Real-time News APIs
```

### **Key Components**

1. **`app.py`**: Main Streamlit application with chat interface and dashboard
2. **`rag_pipeline.py`**: Core RAG logic with LangChain integration
3. **`vector_store.py`**: ChromaDB implementation for semantic search
4. **`news_fetcher.py`**: Multi-API news aggregation system
5. **`config.py`**: Centralized configuration and API settings

## 🎯 **Use Cases**

### **For MSME Business Owners**
- 📈 **Market Intelligence**: Stay updated on sector trends and competitor news
- 💰 **Investment Decisions**: Analyze financial performance and growth potential  
- 🎯 **Strategic Planning**: Understand market positioning and opportunities
- ⚠️ **Risk Assessment**: Monitor risk levels and market changes

### **For Investors & Analysts**
- 🔍 **Due Diligence**: Comprehensive company profiles and financial analysis
- 📊 **Portfolio Monitoring**: Track performance across sectors and companies
- 📰 **Market Research**: Real-time news impact on investment decisions
- 📈 **Trend Analysis**: Identify emerging opportunities and risks

### **For Financial Institutions**
- 💳 **Credit Assessment**: Risk evaluation based on financial metrics
- 🏦 **Loan Portfolio**: Monitor borrower performance and sector health  
- 📋 **Compliance**: Track regulatory changes and market developments
- 🎯 **Business Development**: Identify potential clients and opportunities

## 🔧 **Advanced Configuration**

### **Customizing Sector Keywords**
Edit `config.py` to add or modify sector-specific keywords for better news filtering:

```python
SECTOR_KEYWORDS = {
    "Manufacturing": ["manufacturing", "industrial", "machinery", "automotive"],
    "Technology": ["software", "IT", "digital", "AI", "automation"],
    # Add your custom keywords
}
```

### **Adjusting RAG Parameters**
Modify search parameters in `rag_pipeline.py`:

```python
# Number of context documents to retrieve
base_results = self.vector_store.search_similar(query, n_results=8)

# News article limit
recent_news = self.news_aggregator.fetch_all_news(limit=30)
```

## 🐛 **Troubleshooting**

### **Common Issues**

**"OpenAI API key not found"**
- Ensure you've added `OPENAI_API_KEY` to your `.env` file
- Check that the `.env` file is in the same directory as `app.py`

**"No news articles fetched"**  
- News APIs are optional - the system works without them
- Check your news API keys and rate limits
- Some APIs may have regional restrictions

**"Error loading dashboard data"**
- Ensure your CSV files are in the correct format
- Check that `cleaned_companies.csv` and `cleaned_financial.csv` exist

**"ChromaDB initialization error"**
- Delete the `chroma_db` folder and reinitialize the system
- Ensure you have sufficient disk space

### **Performance Tips**

- **API Rate Limits**: The system includes automatic rate limiting for news APIs
- **Vector Store**: ChromaDB persists data, so reinitialization is faster after the first run
- **Memory**: For large datasets, consider adjusting the context window size
- **Speed**: Disable news fetching for faster responses during testing

## 📈 **Future Enhancements**

- 🔄 **Automated News Refresh**: Scheduled updates to the knowledge base
- 📱 **Mobile Interface**: Responsive design for mobile devices  
- 🌍 **Multi-Language Support**: Hindi and regional language support
- 📊 **Advanced Analytics**: Predictive modeling and trend forecasting
- 🔗 **API Integration**: REST API for external system integration
- 📧 **Alert System**: Email notifications for significant market changes

## 📄 **License**

This project is built for educational and business use. Ensure compliance with all API terms of service.

## 🤝 **Support**

For issues or feature requests, please review the troubleshooting section or check the individual module documentation in the code files.

---

**Built with ❤️ for MSME Market Intelligence**
"""

with open('README.md', 'w') as f:
    f.write(readme_md)

print("README.md created!")