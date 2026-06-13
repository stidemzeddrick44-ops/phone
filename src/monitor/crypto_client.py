import requests

def get_crypto_price(coin_id="bitcoin", vs_currency="usd"):
    """
    Fetches the current price of a cryptocurrency from CoinGecko.
    Default: Bitcoin in USD.
    """
    url = "https://api.coingecko.com/api/v3/simple/price"
    params = {
        "ids": coin_id,
        "vs_currencies": vs_currency
    }
    
    try:
        response = requests.get(url, params=params)
        response.raise_for_status() # Check for errors
        data = response.json()
        return data[coin_id][vs_currency]
    except Exception as e:
        print(f"Error fetching crypto data: {e}")
        return None

if __name__ == "__main__":
    # Test the connection independently
    price = get_crypto_price()
    print(f"Current Bitcoin Price: ${price}")
