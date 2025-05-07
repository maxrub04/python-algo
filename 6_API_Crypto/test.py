import requests
url = "https://api.coingecko.com/api/v3/coins/list"
response = requests.get(url)
coins_list = response.json()
print("The first element of the coin list:", coins_list[10])