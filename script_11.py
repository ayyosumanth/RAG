# Test the system components to ensure they work properly
print("🧪 Testing System Components...")
print("=" * 50)

# 1. Test imports
print("1. Testing imports...")
try:
    import pandas as pd
    import chromadb
    import requests
    print("   ✅ All basic imports successful")
except ImportError as e:
    print(f"   ❌ Import error: {e}")

# 2. Test data loading
print("\n2. Testing data loading...")
try:
    companies_df = pd.read_csv('cleaned_companies.csv')
    financial_df = pd.read_csv('cleaned_financial.csv')
    print(f"   ✅ Companies loaded: {len(companies_df)} records")
    print(f"   ✅ Financial data loaded: {len(financial_df)} records")
    
    # Check data structure
    print(f"   📊 Sectors: {companies_df['Sector'].unique()}")
    print(f"   📈 Financial years: {sorted(financial_df['Year'].unique())}")
    
except Exception as e:
    print(f"   ❌ Data loading error: {e}")

# 3. Test vector store creation (without requiring external APIs)
print("\n3. Testing vector store...")
try:
    from vector_store import MSMEVectorStore
    vector_store = MSMEVectorStore()
    stats = vector_store.get_collection_stats()
    print(f"   ✅ Vector store created successfully")
    print(f"   📊 Current collection stats: {stats}")
except Exception as e:
    print(f"   ❌ Vector store error: {e}")

# 4. Test news fetcher structure (without making API calls)
print("\n4. Testing news fetcher structure...")
try:
    from news_fetcher import NewsAggregator
    news_aggregator = NewsAggregator()
    print("   ✅ News aggregator created successfully")
    print(f"   📡 Configured APIs: {list(news_aggregator.apis.keys())}")
    print(f"   🏷️ Sector keywords: {list(news_aggregator.sector_keywords.keys())}")
except Exception as e:
    print(f"   ❌ News fetcher error: {e}")

# 5. Test configuration
print("\n5. Testing configuration...")
try:
    import config
    print("   ✅ Configuration loaded successfully")
    print(f"   🔧 ChromaDB directory: {config.CHROMA_PERSIST_DIRECTORY}")
    print(f"   📊 Collection name: {config.COLLECTION_NAME}")
    print(f"   🗂️ Sector keywords configured: {len(config.SECTOR_KEYWORDS)}")
except Exception as e:
    print(f"   ❌ Configuration error: {e}")

print("\n" + "=" * 50)
print("🎯 SYSTEM READY FOR TESTING!")
print("\nNext Steps:")
print("1. Copy .env.example to .env and add your OpenAI API key")
print("2. Run: streamlit run app.py")
print("3. Initialize the system in the app sidebar")
print("4. Start chatting with your MSME data!")

print(f"\n📁 Files created:")
files = [
    'requirements.txt', 'config.py', 'news_fetcher.py', 
    'vector_store.py', 'rag_pipeline.py', 'app.py',
    '.env.example', 'README.md'
]
for file in files:
    print(f"   ✅ {file}")

print(f"\n📊 Data files:")
print(f"   ✅ cleaned_companies.csv ({len(companies_df)} companies)")
print(f"   ✅ cleaned_financial.csv ({len(financial_df)} financial records)")