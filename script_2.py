# Create the requirements.txt file
requirements = '''streamlit==1.28.0
langchain==0.0.340
langchain-openai==0.0.1
langchain-community==0.0.7
chromadb==0.4.18
pandas==2.1.3
numpy==1.24.3
requests==2.31.0
python-dotenv==1.0.0
sentence-transformers==2.2.2
openai==1.3.7
plotly==5.17.0
yfinance==0.2.18
beautifulsoup4==4.12.2
lxml==4.9.3
'''

with open('requirements.txt', 'w') as f:
    f.write(requirements)

print("requirements.txt created!")