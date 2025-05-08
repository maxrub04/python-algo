import requests
url = "https://api.coingecko.com/api/v3/coins/list"
response = requests.get(url)
coins_list = response.json()
print("The first element of the coin list:", coins_list[8])



#Obtaining current data on a specific coin
coin_id = "bitcoin"
url = f"https://api.coingecko.com/api/v3/coins/{coin_id}"
params = {
"localization": "false", # Disables translations of cryptocurrency names into other languages.
"tickers": "false", # Disables data on the markets where this coin is traded
"market_data": "true", # Includes current price, capitalisation, volume, etc.
"community_data": "false" # Disables community metrics (number of subscribers, etc.)
,
"developer_data": "false" # Disables GitHub metrics of the project (stars, forks, etc.)
,
"sparkline": "false" # Disables small charts (prices for 7 days)
}
response = requests.get(url, params=params)
bitcoin_data = response.json()
print("Current price of Bitcoin:", bitcoin_data["market_data"]["current_price"]["usd"])


#CoinMarketCap API
url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest"
parameters = {
"symbol": "BTC" # Symbol
}
headers = {
"Accepts": "application/json",
"X-CMC_PRO_API_KEY": "YOUR_API_KEY_HERE" #YOUR_API_KEY_HERE
}
response = requests.get(url, headers=headers, params=parameters)
data = response.json()
print("Current price Bitcoin (CoinMarketCap):", data["data"]["BTC"]["quote"]["USD"]["price"])

#Obtaining global market data
url = "https://pro-api.coinmarketcap.com/v1/global-metrics/quotes/latest"
headers = {
"Accepts": "application/json",
"X-CMC_PRO_API_KEY": "YOUR_API_KEY_HERE"  #YOUR_API_KEY_HERE
}
response = requests.get(url, headers=headers)
global_data = response.json()
print("Total market capitalisation:", global_data["data"]["quote"]["USD"]["total_market_cap"])


#Binance Public API

url = "https://api.binance.com/api/v3/ticker/price"

params = {
"symbol": "BTCUSDT"
}
response = requests.get(url, params=params)
price_data = response.json()
print("Current Price BTC/USDT (Binance):", price_data["price"])

#Obtaining historical data (Kline/Candlestick data)

url = "https://api.binance.com/api/v3/klines"
params = {
"symbol": "BTCUSDT",
"interval": "1h", "limit": 10 # timeframe -1h + 10 last candles
}
response = requests.get(url, params=params)
klines = response.json()

print("First Candle (timestamp, open, high, low, close):", klines[0][:5])


#Order-Book
url = "https://api.binance.com/api/v3/depth"
params = {
"symbol": "BTCUSDT",
"limit": 5 # top 5 orders
}
response = requests.get(url, params=params)
order_book = response.json()
print("First 5 BUY orders:", order_book["bids"])
print("First 5 SELL oders:", order_book["asks"])


"""
try:
response = requests.get(url, params=params)
response.raise_for_status() # If the status code is 4xx or 5xx, an error is generated
data = response.json()
except requests.exceptions.HTTPError as http_err:
print(f"HTTP error: {http_err}")
except Exception as err:
print(f"Error: {err}")
"""
