# Create .env.example file for environment variables template
env_example = """# MSME RAG Chatbot API Keys
# Copy this file to .env and add your actual API keys

# Required for AI responses (GET FROM: https://platform.openai.com/api-keys)
OPENAI_API_KEY=your_openai_api_key_here

# Optional News APIs (for enhanced market intelligence)
# GET FROM: https://newsdata.io/
NEWSDATA_API_KEY=your_newsdata_api_key_here

# GET FROM: https://finnhub.io/
FINNHUB_API_KEY=your_finnhub_api_key_here

# GET FROM: https://www.alphavantage.co/
ALPHA_VANTAGE_API_KEY=your_alpha_vantage_api_key_here

# GET FROM: https://www.marketaux.com/
MARKETAUX_API_KEY=your_marketaux_api_key_here
"""

with open('.env.example', 'w') as f:
    f.write(env_example)

print(".env.example created!")