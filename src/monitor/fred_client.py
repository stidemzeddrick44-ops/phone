import os
import requests
from dotenv import load_dotenv

# Load variables from the root .env file
load_dotenv(dotenv_path="../../.env")

def get_economic_data(series_id):
    api_key = os.getenv("FRED_API_KEY")
    base_url = "https://api.stlouisfed.org/fred/series/observations"
    
    params = {
        "series_id": series_id,
        "api_key": api_key,
        "file_type": "json"
    }
    
    response = requests.get(base_url, params=params)
    return response.json()

if __name__ == "__main__":
    # Example: CPI (Consumer Price Index)
    data = get_economic_data("CPIAUCSL")
    print(data)
