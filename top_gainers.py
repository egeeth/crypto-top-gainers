import requests

def fetch_top_gainers(limit=10):
    url = "https://api.coingecko.com/api/v3/coins/markets"
    params = {
        "vs_currency": "usd",
        "order": "price_change_percentage_24h_desc",
        "per_page": limit,
        "page": 1,
        "sparkline": "false"
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        coins = response.json()
        print("Son 24 saatte en çok yükselen coinler:")
        for i, coin in enumerate(coins, 1):
            name = coin.get("name")
            symbol = coin.get("symbol").upper()
            change = coin.get("price_change_percentage_24h")
            price = coin.get("current_price")
            print(f"{i}. {name} ({symbol}) | Fiyat: ${price} | 24s Değişim: %{change:.2f}")
    else:
        print("Coin verileri alınamadı.")

if __name__ == "__main__":
    fetch_top_gainers()