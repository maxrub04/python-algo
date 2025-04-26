price= 3500
change = 3500 *0.02
name = "BTC"
ACTIVE_TRADE = False


prices=[3500,3600,3700]
prices.append(price)
for price in prices:
    print(price)

coins={
    "BTC":{"name":"Bitcoin","price": 35000},
    "ETH":{"name":"Etherium","price": 2200},
}
coins["LTH"]={"name":"Litecoin","price": 20000}
for coin in coins:
    print(coins[coin]["name"],coins[coin]["price"])


assets=("Binance","USDT","spot")
print(f"Market assets: {assets[0]}")

trade_ids = {101, 102, 103, 101}
print("Уникальные id сделок:", trade_ids)

user_price = int(input("enter the price: "))
def prices(user_price):

    if user_price > price:
        print("Цена выше порога")
    elif user_price < price:
        print("Цена ниже порога")
    elif user_price == price:
        print("Цена равна порогу")

prices(user_price)


numbers=[1,2,3,4,5]

for num in numbers:
    print(f"kvadrat chisla {num} == {num ** 2}")


count = 0

while count <=5:
    print(f"number of interations = {count}")
    count+=1


