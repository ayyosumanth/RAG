import os
from dotenv import load_dotenv

load_dotenv()

# API Keys - Add these to your .env file
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
NEWSDATA_API_KEY = os.getenv("NEWSDATA_API_KEY")
FINNHUB_API_KEY = os.getenv("FINNHUB_API_KEY")
ALPHA_VANTAGE_API_KEY = os.getenv("ALPHA_VANTAGE_API_KEY")
MARKETAUX_API_KEY = os.getenv("MARKETAUX_API_KEY")

# News API Endpoints
NEWS_APIS = {
    "newsdata": {
        "url": "https://newsdata.io/api/1/news",
        "key": NEWSDATA_API_KEY,
        "params": {
            "apikey": NEWSDATA_API_KEY,
            "country": "in",
            "language": "en",
            "category": "business,technology",
            "size": 10
        }
    },
    "finnhub": {
        "url": "https://finnhub.io/api/v1/news",
        "key": FINNHUB_API_KEY,
        "params": {
            "token": FINNHUB_API_KEY,
            "category": "general"
        }
    },
    "alpha_vantage": {
        "url": "https://www.alphavantage.co/query",
        "key": ALPHA_VANTAGE_API_KEY,
        "params": {
            "function": "NEWS_SENTIMENT",
            "apikey": ALPHA_VANTAGE_API_KEY,
            "topics": "technology,earnings",
            "limit": 50
        }
    },
    "marketaux": {
        "url": "https://api.marketaux.com/v1/news/all",
        "key": MARKETAUX_API_KEY,
        "params": {
            "api_token": MARKETAUX_API_KEY,
            "countries": "in",
            "filter_entities": "true",
            "language": "en",
            "limit": 10
        }
    }
}

# MSME Sector Keywords for filtering
SECTOR_KEYWORDS = {
    "Manufacturing": ["manufacturing", "industrial", "machinery", "metal", "automotive", "precision", "equipment"],
    "Food Processing": ["food", "beverage", "dairy", "snacks", "organic", "nutrition", "restaurant", "catering"],
    "Technology": ["software", "IT", "tech", "digital", "app", "platform", "AI", "automation", "cloud"],
    "Healthcare": ["healthcare", "pharmaceutical", "medical", "biotech", "hospital", "clinic", "diagnostic"],
    "Textiles": ["textile", "garment", "fabric", "apparel", "fashion", "clothing", "cotton", "fiber"]
}

# ChromaDB Settings
CHROMA_PERSIST_DIRECTORY = "./chroma_db"
COLLECTION_NAME = "msme_knowledge_base"

# Streamlit Configuration
PAGE_CONFIG = {
    "page_title": "MSME News & Market Intelligence",
    "page_icon": "📊",
    "layout": "wide",
    "initial_sidebar_state": "expanded"
}
