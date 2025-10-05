import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta
import time
import os

# Import our custom modules
try:
    from rag_pipeline import MSMERAGPipeline
    from vector_store import MSMEVectorStore
    from news_fetcher import NewsAggregator
    import config
except ImportError as e:
    st.error(f"Error importing modules: {str(e)}")
    st.stop()

# Page configuration
st.set_page_config(**config.PAGE_CONFIG)

# Custom CSS
st.markdown("""
<style>
    .main-header {
        color: #1f77b4;
        text-align: center;
        padding: 1rem 0;
        border-bottom: 3px solid #1f77b4;
        margin-bottom: 2rem;
    }
    .sector-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 1rem;
        border-radius: 10px;
        margin: 0.5rem 0;
    }
    .metric-card {
        background: #f8f9fa;
        padding: 1rem;
        border-radius: 8px;
        border-left: 4px solid #28a745;
        margin: 0.5rem 0;
    }
    .chat-container {
        max-height: 600px;
        overflow-y: auto;
        background: #f8f9fa;
        padding: 1rem;
        border-radius: 10px;
        margin: 1rem 0;
    }
    .user-message {
        background: #007bff;
        color: white;
        padding: 0.8rem;
        border-radius: 15px 15px 5px 15px;
        margin: 0.5rem 0;
        max-width: 80%;
        float: right;
        clear: both;
    }
    .assistant-message {
        background: #e9ecef;
        color: #333;
        padding: 0.8rem;
        border-radius: 15px 15px 15px 5px;
        margin: 0.5rem 0;
        max-width: 80%;
        float: left;
        clear: both;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state
if 'rag_pipeline' not in st.session_state:
    st.session_state.rag_pipeline = None
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []
if 'knowledge_base_loaded' not in st.session_state:
    st.session_state.knowledge_base_loaded = False

# Header
st.markdown('<h1 class="main-header">🏭 MSME Market Intelligence & News Aggregator</h1>', 
           unsafe_allow_html=True)

# Sidebar
st.sidebar.title("🔧 Configuration")

# API Key Configuration
st.sidebar.subheader("API Configuration")
api_status = {}

# Check API keys
openai_key = st.sidebar.text_input("OpenAI API Key", 
                                  value=os.getenv('OPENAI_API_KEY', ''), 
                                  type="password",
                                  help="Required for AI responses")

newsdata_key = st.sidebar.text_input("NewsData.io API Key", 
                                    value=os.getenv('NEWSDATA_API_KEY', ''), 
                                    type="password",
                                    help="For Indian business news")

finnhub_key = st.sidebar.text_input("Finnhub API Key", 
                                   value=os.getenv('FINNHUB_API_KEY', ''), 
                                   type="password",
                                   help="For financial market news")

alpha_vantage_key = st.sidebar.text_input("Alpha Vantage API Key", 
                                         value=os.getenv('ALPHA_VANTAGE_API_KEY', ''), 
                                         type="password",
                                         help="For news sentiment analysis")

marketaux_key = st.sidebar.text_input("MarketAux API Key", 
                                     value=os.getenv('MARKETAUX_API_KEY', ''), 
                                     type="password",
                                     help="For market news")

# Update environment variables
if openai_key:
    os.environ['OPENAI_API_KEY'] = openai_key
if newsdata_key:
    os.environ['NEWSDATA_API_KEY'] = newsdata_key
if finnhub_key:
    os.environ['FINNHUB_API_KEY'] = finnhub_key
if alpha_vantage_key:
    os.environ['ALPHA_VANTAGE_API_KEY'] = alpha_vantage_key
if marketaux_key:
    os.environ['MARKETAUX_API_KEY'] = marketaux_key

# Display API status
for api_name, key in [("OpenAI", openai_key), ("NewsData.io", newsdata_key), 
                      ("Finnhub", finnhub_key), ("Alpha Vantage", alpha_vantage_key),
                      ("MarketAux", marketaux_key)]:
    status = "✅ Connected" if key else "❌ Not configured"
    st.sidebar.write(f"**{api_name}**: {status}")

# Initialize RAG Pipeline
if st.sidebar.button("🚀 Initialize System") and openai_key:
    with st.spinner("Initializing RAG Pipeline..."):
        try:
            st.session_state.rag_pipeline = MSMERAGPipeline()

            # Load knowledge base if data files exist
            if os.path.exists('cleaned_companies.csv') and os.path.exists('cleaned_financial.csv'):
                st.session_state.rag_pipeline.initialize_knowledge_base(
                    'cleaned_companies.csv', 
                    'cleaned_financial.csv'
                )
                st.session_state.knowledge_base_loaded = True
                st.sidebar.success("✅ System initialized successfully!")
            else:
                st.sidebar.error("❌ Data files not found. Please ensure 'cleaned_companies.csv' and 'cleaned_financial.csv' are present.")

        except Exception as e:
            st.sidebar.error(f"❌ Error initializing system: {str(e)}")

# Main content area
if not st.session_state.rag_pipeline:
    st.info("👆 Please configure API keys and initialize the system using the sidebar.")

    # Show setup instructions
    st.subheader("🔧 Setup Instructions")

    st.markdown("""
    **Step 1: Get API Keys**
    - **OpenAI API Key** (Required): Get from [OpenAI Platform](https://platform.openai.com/api-keys)
    - **NewsData.io API Key** (Optional): Get from [NewsData.io](https://newsdata.io/)
    - **Finnhub API Key** (Optional): Get from [Finnhub](https://finnhub.io/)
    - **Alpha Vantage API Key** (Optional): Get from [Alpha Vantage](https://www.alphavantage.co/)
    - **MarketAux API Key** (Optional): Get from [MarketAux](https://www.marketaux.com/)

    **Step 2: Enter API Keys**
    - Enter your API keys in the sidebar
    - At minimum, you need the OpenAI API key for the chatbot to work
    - News APIs are optional but provide real-time market intelligence

    **Step 3: Initialize System**
    - Click "🚀 Initialize System" in the sidebar
    - The system will load your MSME company data and fetch recent news
    - Wait for the success message

    **Step 4: Start Chatting**
    - Use the chat interface to ask questions about MSME companies
    - Ask for company analysis, sector trends, financial comparisons, etc.
    """)

    # Show sample data preview
    st.subheader("📊 Your MSME Dataset Preview")

    try:
        companies_df = pd.read_csv('cleaned_companies.csv')
        st.write(f"**Companies loaded:** {len(companies_df)}")

        col1, col2 = st.columns(2)
        with col1:
            st.write("**Sectors:**")
            sector_counts = companies_df['Sector'].value_counts()
            st.write(sector_counts)

        with col2:
            st.write("**Sample Companies:**")
            st.write(companies_df[['Company_Name', 'Sector', 'Location']].head())

        # Show financial data preview
        try:
            financial_df = pd.read_csv('cleaned_financial.csv')
            st.write(f"**Financial records:** {len(financial_df)}")
            st.write("Latest financial data sample:")
            st.write(financial_df.head())
        except:
            st.warning("Financial data file not found.")

    except Exception as e:
        st.error(f"Could not load data preview: {str(e)}")

else:
    # Main application interface
    tab1, tab2, tab3, tab4 = st.tabs(["💬 Chat Assistant", "📊 Dashboard", "📰 News Feed", "📈 Analytics"])

    with tab1:
        st.subheader("🤖 MSME Market Intelligence Assistant")

        # Chat interface
        st.markdown('<div class="chat-container">', unsafe_allow_html=True)

        # Display chat history
        for message in st.session_state.chat_history:
            if message["role"] == "user":
                st.markdown(f'<div class="user-message">{message["content"]}</div>', 
                           unsafe_allow_html=True)
            else:
                st.markdown(f'<div class="assistant-message">{message["content"]}</div>', 
                           unsafe_allow_html=True)

        st.markdown('</div>', unsafe_allow_html=True)

        # Chat input
        if prompt := st.chat_input("Ask about MSME companies, market trends, financial analysis..."):
            # Add user message to history
            st.session_state.chat_history.append({"role": "user", "content": prompt})

            # Process query
            with st.spinner("Analyzing your question..."):
                try:
                    response = st.session_state.rag_pipeline.process_query(prompt)
                    st.session_state.chat_history.append({"role": "assistant", "content": response})

                    # Rerun to update chat display
                    st.rerun()

                except Exception as e:
                    st.error(f"Error processing query: {str(e)}")

        # Quick action buttons
        st.subheader("🚀 Quick Actions")
        col1, col2, col3 = st.columns(3)

        with col1:
            if st.button("📊 Manufacturing Overview"):
                with st.spinner("Getting manufacturing sector overview..."):
                    response = st.session_state.rag_pipeline.get_sector_summary("Manufacturing")
                    st.session_state.chat_history.append({"role": "user", "content": "Manufacturing sector overview"})
                    st.session_state.chat_history.append({"role": "assistant", "content": response})
                    st.rerun()

        with col2:
            if st.button("💡 Technology Trends"):
                with st.spinner("Analyzing technology sector trends..."):
                    response = st.session_state.rag_pipeline.get_sector_summary("Technology")
                    st.session_state.chat_history.append({"role": "user", "content": "Technology sector trends"})
                    st.session_state.chat_history.append({"role": "assistant", "content": response})
                    st.rerun()

        with col3:
            if st.button("🏥 Healthcare Analysis"):
                with st.spinner("Getting healthcare sector analysis..."):
                    response = st.session_state.rag_pipeline.get_sector_summary("Healthcare")
                    st.session_state.chat_history.append({"role": "user", "content": "Healthcare sector analysis"})
                    st.session_state.chat_history.append({"role": "assistant", "content": response})
                    st.rerun()

        # Clear chat button
        if st.button("🗑️ Clear Chat History"):
            st.session_state.chat_history = []
            st.session_state.rag_pipeline.clear_history()
            st.rerun()

    with tab2:
        st.subheader("📊 MSME Performance Dashboard")

        # Load and display data
        try:
            companies_df = pd.read_csv('cleaned_companies.csv')
            financial_df = pd.read_csv('cleaned_financial.csv')

            # Key metrics
            col1, col2, col3, col4 = st.columns(4)

            with col1:
                st.metric("Total Companies", len(companies_df))

            with col2:
                avg_employees = companies_df['Employee_Count'].mean()
                st.metric("Avg Employees", f"{avg_employees:.0f}")

            with col3:
                latest_revenue = financial_df[financial_df['Year'] == financial_df['Year'].max()]['Revenue_Crores'].sum()
                st.metric("Total Revenue (2024)", f"₹{latest_revenue:.1f}Cr")

            with col4:
                avg_profit_margin = financial_df[financial_df['Year'] == financial_df['Year'].max()]['Profit_Margin_Percent'].mean()
                st.metric("Avg Profit Margin", f"{avg_profit_margin:.1f}%")

            # Sector distribution
            st.subheader("Sector Distribution")
            sector_fig = px.pie(companies_df, names='Sector', title="Companies by Sector")
            st.plotly_chart(sector_fig, use_container_width=True)

            # Financial performance by sector
            st.subheader("Financial Performance by Sector (2024)")
            financial_2024 = financial_df[financial_df['Year'] == 2024]
            merged_df = financial_2024.merge(companies_df[['Company_ID', 'Sector']], on='Company_ID')

            sector_performance = merged_df.groupby('Sector').agg({
                'Revenue_Crores': 'mean',
                'Profit_Margin_Percent': 'mean',
                'ROA_Percent': 'mean'
            }).round(2)

            st.write(sector_performance)

            # Revenue trends
            st.subheader("Revenue Trends Over Time")
            revenue_trends = financial_df.merge(companies_df[['Company_ID', 'Sector']], on='Company_ID')
            sector_yearly = revenue_trends.groupby(['Year', 'Sector'])['Revenue_Crores'].mean().reset_index()

            trend_fig = px.line(sector_yearly, x='Year', y='Revenue_Crores', 
                              color='Sector', title="Average Revenue Trends by Sector")
            st.plotly_chart(trend_fig, use_container_width=True)

        except Exception as e:
            st.error(f"Error loading dashboard data: {str(e)}")

    with tab3:
        st.subheader("📰 Latest Market News")

        if st.button("🔄 Refresh News"):
            with st.spinner("Fetching latest news..."):
                try:
                    news_aggregator = NewsAggregator()
                    all_news = news_aggregator.fetch_all_news(limit=20)

                    if all_news:
                        st.session_state.latest_news = all_news
                        st.success(f"Fetched {len(all_news)} news articles")
                    else:
                        st.warning("No news articles fetched. Check your API keys.")

                except Exception as e:
                    st.error(f"Error fetching news: {str(e)}")

        # Display news
        if hasattr(st.session_state, 'latest_news'):
            for i, article in enumerate(st.session_state.latest_news):
                with st.expander(f"📰 {article.get('title', 'No Title')[:100]}..."):
                    col1, col2 = st.columns([3, 1])

                    with col1:
                        st.write(f"**Source:** {article.get('source_name', 'Unknown')}")
                        st.write(f"**Category:** {article.get('category', 'business').title()}")
                        if article.get('published_at'):
                            st.write(f"**Published:** {article.get('published_at')}")

                        if article.get('description'):
                            st.write("**Description:**")
                            st.write(article['description'])

                        if article.get('url'):
                            st.write(f"[Read Full Article]({article['url']})")

                    with col2:
                        if article.get('sentiment'):
                            sentiment_color = {"positive": "🟢", "negative": "🔴", "neutral": "🟡"}
                            sentiment_icon = sentiment_color.get(article['sentiment'].lower(), "🟡")
                            st.write(f"**Sentiment:** {sentiment_icon} {article['sentiment'].title()}")

                            if article.get('sentiment_score'):
                                st.write(f"**Score:** {article['sentiment_score']:.2f}")
        else:
            st.info("Click 'Refresh News' to fetch latest market updates.")

    with tab4:
        st.subheader("📈 Advanced Analytics")

        try:
            companies_df = pd.read_csv('cleaned_companies.csv')
            financial_df = pd.read_csv('cleaned_financial.csv')

            # Performance scoring analysis
            st.subheader("Performance Score Analysis")

            performance_cols = ['Financial_Performance_Score', 'Operational_Efficiency_Score', 
                              'Market_Position_Score', 'Innovation_Score']

            if all(col in companies_df.columns for col in performance_cols):
                score_data = companies_df.groupby('Sector')[performance_cols].mean()

                score_fig = go.Figure()

                for col in performance_cols:
                    score_fig.add_trace(go.Scatter(
                        x=score_data.index,
                        y=score_data[col],
                        mode='lines+markers',
                        name=col.replace('_Score', '').replace('_', ' ')
                    ))

                score_fig.update_layout(title="Performance Scores by Sector",
                                      xaxis_title="Sector",
                                      yaxis_title="Score")

                st.plotly_chart(score_fig, use_container_width=True)

            # Risk analysis
            st.subheader("Risk Level Distribution")
            if 'Risk_Level' in companies_df.columns:
                risk_counts = companies_df['Risk_Level'].value_counts()
                risk_fig = px.bar(x=risk_counts.index, y=risk_counts.values, 
                                title="Companies by Risk Level")
                st.plotly_chart(risk_fig, use_container_width=True)

            # Growth analysis
            st.subheader("Growth Analysis")
            financial_with_sector = financial_df.merge(companies_df[['Company_ID', 'Sector']], on='Company_ID')

            # Calculate growth rates
            growth_data = []
            for sector in financial_with_sector['Sector'].unique():
                sector_data = financial_with_sector[financial_with_sector['Sector'] == sector]

                revenue_2022 = sector_data[sector_data['Year'] == 2022]['Revenue_Crores'].sum()
                revenue_2024 = sector_data[sector_data['Year'] == 2024]['Revenue_Crores'].sum()

                if revenue_2022 > 0:
                    growth_rate = ((revenue_2024 - revenue_2022) / revenue_2022) * 100
                    growth_data.append({'Sector': sector, 'Growth_Rate': growth_rate})

            if growth_data:
                growth_df = pd.DataFrame(growth_data)
                growth_fig = px.bar(growth_df, x='Sector', y='Growth_Rate',
                                  title="Revenue Growth Rate 2022-2024 (%)")
                st.plotly_chart(growth_fig, use_container_width=True)

        except Exception as e:
            st.error(f"Error in analytics: {str(e)}")

# Footer
st.markdown("---")
st.markdown("**MSME Market Intelligence Platform** | Built with Streamlit, LangChain & ChromaDB")
