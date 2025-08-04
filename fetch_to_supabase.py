from pycoingecko import CoinGeckoAPI
from supabase_config import supabase
from datetime import datetime


# Initialize CoinGecko API
cg = CoinGeckoAPI()

# List of coins to track
coins = ['bitcoin', 'ethereum', 'solana']

def fetch_and_store():
    try:
        # Fetch current prices
        data = cg.get_price(ids=coins, vs_currencies='usd')

        for coin in coins:
            name = coin.capitalize()
            symbol = coin[:3].upper()
            price = data[coin]['usd']
            now = datetime.utcnow().isoformat()

            # Insert into Supabase table
            supabase.table("crypto_prices").insert({
                "name": name,
                "symbol": symbol,
                "price_usd": price,
                "timestamp": now
            }).execute()

        print("✅ Prices updated successfully.")

    except Exception as e:
        print("❌ Error fetching or storing data:", e)

# Run the function
if __name__ == "__main__":
    fetch_and_store()