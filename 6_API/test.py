import requests
url = "https://api.coingecko.com/api/v3/coins/list"
response = requests.get(url)
coins_list = response.json()
print("The first element of the coin list:", coins_list[8])



#Obtaining current data on a specific coin
coin_id = "bitcoin"
url = f"https://api.coingecko.com/api/v3/coins/{coin_id}"
params = {
"localization": "false", # Отключить локализованные данные
"tickers": "false", # Отключить тиканье (ticker data)
"market_data": "true", # Включить рыночные данные
"community_data": "false"
,
"developer_data": "false"
,
"sparkline": "false"
}
response = requests.get(url, params=params)
bitcoin_data = response.json()
print("Current price of Bitcoin:", bitcoin_data["market_data"]["current_price"]["usd"])