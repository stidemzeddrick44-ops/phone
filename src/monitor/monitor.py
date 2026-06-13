# monitor.py
# This script will eventually track global economic trends.
# For now, let's verify our monitoring system is live.

def initialize_monitor():
    print("Monitor system initialized: Ready to track global economic data.")

if __name__ == "__main__":
    initialize_monitor()
import crypto_client
import news_client
import sentiment_client
import db_client
import sqlite3

def run_monitor():
    print("Starting system monitor...")

    # 1. Fetch data from specialists
    btc_price = crypto_client.get_crypto_price("bitcoin")
    news_items = news_client.get_market_news("bitcoin")

    # 2. Process with the "Brain"
    if news_items:
        # We analyze the first headline's sentiment
        latest_headline = news_items[0]['title']
        sentiment_score = sentiment_client.analyze_sentiment(latest_headline)
        print(f"Headline: {latest_headline} | Sentiment: 
  {sentiment_score}")
    else:
        sentiment_score = 0
        print("No news found.")

    # 3. Store in Memory
    conn = sqlite3.connect("monitor_data.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO market_data (source, symbol, price) VALUES (?, ?, ?)", 
                   ("CoinGecko/NewsAPI", "BTC", btc_price))
    conn.commit()
    conn.close()
    
    print("Cycle complete: Data saved to database.")

if __name__ == "__main__":
    run_monitor()
