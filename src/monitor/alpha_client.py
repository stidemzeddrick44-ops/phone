import os
import requests
from dotenv import load_dotenv

# This tells the code where to find your secret keys
load_dotenv(dotenv_path="../../.env")

def get_stock_quote(symbol):
    # This retrieves your key from the .env file
    api_key = os.getenv("ALPHA_VANTAGE_KEY")
    url = f"https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={symbol}&apikey={api_key}"
    
    response = requests.get(url)
    return response.json()

# This is a simple test to make sure it works
if __name__ == "__main__":
    print(get_stock_quote("IBM"))
