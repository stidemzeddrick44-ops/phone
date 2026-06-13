import os
import requests
from dotenv import load_dotenv

# Load your secret key from the .env file
load_dotenv(dotenv_path="../../.env")

def get_market_news(query="finance"):
    """
    Fetches the latest headlines related to a specific topic.
    """
    api_key = os.getenv("NEWS_API_KEY")
    url = f"https://newsapi.org/v2/everything?q={query}&apiKey={api_key}"
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        articles = response.json().get('articles', [])
        # Return the top 3 headlines
        return articles[:3]
    except Exception as e:
        print(f"Error fetching news: {e}")
        return []

if __name__ == "__main__":
    # Test the connection
    news = get_market_news("crypto")
    for article in news:
        print(f"- {article['title']}")
