import requests
import time

def fetch_hyperliquid_funding_rates():
    """
    Basic synchronous function to fetch current funding rates from Hyperliquid.
    For a production Delta-Neutral bot, this MUST be handled asynchronously via WebSockets.
    """
    print("Fetching real-time funding rates from Hyperliquid API...")
    url = "https://api.hyperliquid.xyz/info"
    
    headers = {"Content-Type": "application/json"}
    payload = {"type": "metaAndAssetCtxs"}
    
    try:
        response = requests.post(url, headers=headers, json=payload)
        data = response.json()
        
        # The API returns an array, index 1 contains the asset contexts (funding rates)
        asset_contexts = data[1]
        
        print("\n--- Top Funding Rates ---")
        for idx, asset in enumerate(asset_contexts):
            funding_rate = float(asset['funding']) * 100 * 24 # Annualized approx
            if abs(funding_rate) > 10.0: # Only show interesting rates
                # Note: To match this with actual coin names, you need the 'meta' dictionary (index 0)
                print(f"Asset Index {idx} | Approx APR: {funding_rate:.2f}%")
                
    except Exception as e:
        print(f"Connection error: {e}")

if __name__ == "__main__":
    fetch_hyperliquid_funding_rates()
    print("\n[!] To execute a Delta-Neutral strategy safely, you need concurrent Async execution.")
    print("[!] Check the README to get the production-ready boilerplate.")
