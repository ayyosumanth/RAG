# Create news_fetcher.py - Multi-API news integration
news_fetcher_py = '''import requests
import json
from datetime import datetime, timedelta
from typing import List, Dict, Any
import config
import time

class NewsAggregator:
    """
    Multi-API news aggregator for MSME market intelligence
    """
    
    def __init__(self):
        self.apis = config.NEWS_APIS
        self.sector_keywords = config.SECTOR_KEYWORDS
        
    def fetch_newsdata_io(self, query_keywords: List[str] = None) -> List[Dict]:
        """Fetch news from NewsData.io API"""
        try:
            params = self.apis["newsdata"]["params"].copy()
            if query_keywords:
                params["q"] = " OR ".join(query_keywords[:5])  # Limit keywords
                
            response = requests.get(self.apis["newsdata"]["url"], params=params, timeout=10)
            
            if response.status_code == 200:
                data = response.json()
                articles = []
                
                for article in data.get("results", []):
                    articles.append({
                        "source": "NewsData.io",
                        "title": article.get("title", ""),
                        "description": article.get("description", ""),
                        "content": article.get("content", ""),
                        "url": article.get("link", ""),
                        "published_at": article.get("pubDate", ""),
                        "source_name": article.get("source_id", ""),
                        "category": article.get("category", ["business"])[0] if article.get("category") else "business"
                    })
                return articles
            else:
                print(f"NewsData.io API error: {response.status_code}")
                return []
                
        except Exception as e:
            print(f"Error fetching NewsData.io: {str(e)}")
            return []
    
    def fetch_finnhub(self, symbol: str = None) -> List[Dict]:
        """Fetch financial news from Finnhub"""
        try:
            params = self.apis["finnhub"]["params"].copy()
            if symbol:
                params["symbol"] = symbol
                
            response = requests.get(self.apis["finnhub"]["url"], params=params, timeout=10)
            
            if response.status_code == 200:
                articles_data = response.json()
                articles = []
                
                for article in articles_data:
                    articles.append({
                        "source": "Finnhub",
                        "title": article.get("headline", ""),
                        "description": article.get("summary", ""),
                        "content": article.get("summary", ""),
                        "url": article.get("url", ""),
                        "published_at": datetime.fromtimestamp(article.get("datetime", 0)).isoformat(),
                        "source_name": article.get("source", ""),
                        "category": "financial"
                    })
                return articles
            else:
                print(f"Finnhub API error: {response.status_code}")
                return []
                
        except Exception as e:
            print(f"Error fetching Finnhub: {str(e)}")
            return []
    
    def fetch_alpha_vantage(self, topics: List[str] = None) -> List[Dict]:
        """Fetch news with sentiment from Alpha Vantage"""
        try:
            params = self.apis["alpha_vantage"]["params"].copy()
            if topics:
                params["topics"] = ",".join(topics[:3])  # Limit topics
                
            response = requests.get(self.apis["alpha_vantage"]["url"], params=params, timeout=15)
            
            if response.status_code == 200:
                data = response.json()
                articles = []
                
                feed = data.get("feed", [])
                for article in feed[:10]:  # Limit to 10 articles
                    articles.append({
                        "source": "Alpha Vantage",
                        "title": article.get("title", ""),
                        "description": article.get("summary", ""),
                        "content": article.get("summary", ""),
                        "url": article.get("url", ""),
                        "published_at": article.get("time_published", ""),
                        "source_name": article.get("source", ""),
                        "category": "market_sentiment",
                        "sentiment": article.get("overall_sentiment_label", "neutral"),
                        "sentiment_score": article.get("overall_sentiment_score", 0.0)
                    })
                return articles
            else:
                print(f"Alpha Vantage API error: {response.status_code}")
                return []
                
        except Exception as e:
            print(f"Error fetching Alpha Vantage: {str(e)}")
            return []
    
    def fetch_marketaux(self, keywords: List[str] = None) -> List[Dict]:
        """Fetch news from MarketAux API"""
        try:
            params = self.apis["marketaux"]["params"].copy()
            if keywords:
                params["search"] = " ".join(keywords[:3])
                
            response = requests.get(self.apis["marketaux"]["url"], params=params, timeout=10)
            
            if response.status_code == 200:
                data = response.json()
                articles = []
                
                for article in data.get("data", []):
                    articles.append({
                        "source": "MarketAux",
                        "title": article.get("title", ""),
                        "description": article.get("description", ""),
                        "content": article.get("snippet", ""),
                        "url": article.get("url", ""),
                        "published_at": article.get("published_at", ""),
                        "source_name": article.get("source", ""),
                        "category": "market_news"
                    })
                return articles
            else:
                print(f"MarketAux API error: {response.status_code}")
                return []
                
        except Exception as e:
            print(f"Error fetching MarketAux: {str(e)}")
            return []
    
    def fetch_sector_news(self, sector: str, limit: int = 20) -> List[Dict]:
        """Fetch news for a specific MSME sector"""
        sector_keywords = self.sector_keywords.get(sector, [])
        all_articles = []
        
        # Fetch from all APIs
        print(f"Fetching news for {sector} sector...")
        
        # NewsData.io
        articles_newsdata = self.fetch_newsdata_io(sector_keywords)
        all_articles.extend(articles_newsdata)
        time.sleep(1)  # Rate limiting
        
        # Finnhub (general financial news)
        articles_finnhub = self.fetch_finnhub()
        all_articles.extend(articles_finnhub)
        time.sleep(1)
        
        # Alpha Vantage
        articles_alpha = self.fetch_alpha_vantage([sector.lower()])
        all_articles.extend(articles_alpha)
        time.sleep(1)
        
        # MarketAux
        articles_market = self.fetch_marketaux(sector_keywords)
        all_articles.extend(articles_market)
        
        # Filter and deduplicate
        filtered_articles = self._filter_by_relevance(all_articles, sector_keywords)
        
        return filtered_articles[:limit]
    
    def fetch_all_news(self, limit: int = 50) -> List[Dict]:
        """Fetch general business and market news"""
        all_articles = []
        
        print("Fetching general business news...")
        
        # Fetch from all APIs
        articles_newsdata = self.fetch_newsdata_io()
        all_articles.extend(articles_newsdata)
        time.sleep(1)
        
        articles_finnhub = self.fetch_finnhub()
        all_articles.extend(articles_finnhub)
        time.sleep(1)
        
        articles_alpha = self.fetch_alpha_vantage()
        all_articles.extend(articles_alpha)
        time.sleep(1)
        
        articles_market = self.fetch_marketaux()
        all_articles.extend(articles_market)
        
        # Remove duplicates and sort by date
        unique_articles = self._deduplicate_articles(all_articles)
        
        return unique_articles[:limit]
    
    def _filter_by_relevance(self, articles: List[Dict], keywords: List[str]) -> List[Dict]:
        """Filter articles by keyword relevance"""
        filtered = []
        keywords_lower = [k.lower() for k in keywords]
        
        for article in articles:
            title = article.get("title", "").lower()
            description = article.get("description", "").lower()
            content = article.get("content", "").lower()
            
            # Check if any keyword appears in title, description, or content
            if any(keyword in title or keyword in description or keyword in content 
                   for keyword in keywords_lower):
                filtered.append(article)
        
        return filtered
    
    def _deduplicate_articles(self, articles: List[Dict]) -> List[Dict]:
        """Remove duplicate articles based on title similarity"""
        unique_articles = []
        seen_titles = set()
        
        for article in articles:
            title = article.get("title", "").lower().strip()
            if title and title not in seen_titles:
                seen_titles.add(title)
                unique_articles.append(article)
        
        # Sort by published date (most recent first)
        try:
            unique_articles.sort(
                key=lambda x: datetime.fromisoformat(x.get("published_at", "").replace("Z", "+00:00")),
                reverse=True
            )
        except:
            pass  # Keep original order if date parsing fails
        
        return unique_articles

# Test the news fetcher
if __name__ == "__main__":
    # This is for testing - requires API keys in .env file
    fetcher = NewsAggregator()
    print("News Aggregator created successfully!")
'''

with open('news_fetcher.py', 'w') as f:
    f.write(news_fetcher_py)

print("news_fetcher.py created!")