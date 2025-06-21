import requests
import time
import hmac
import hashlib
from urllib.parse import urlencode
api_key = "YOUR_API_KEY"
api_secret = "YOUR_API_SECRET"
def send_order(symbol, side, order_type, quantity, price=None):

    base_url = "https://api.binance.com"
    endpoint = "/api/v3/order"
    params = {

        "symbol": symbol,
        "side": side, # "BUY" или "SELL"
        "type": order_type, # Например, "LIMIT"
        "quantity": quantity,
        "timestamp": int(time.time() * 1000)
        }
    if price is not None:
        params["price"] = price
        params["timeInForce"] = "GTC"

    query_string = urlencode(params)
    signature = hmac.new(api_secret.encode('utf-8'),
        query_string.encode('utf-8'),
        hashlib.sha256).hexdigest()
    params["signature"] = signature

    headers = {
    "X-MBX-APIKEY": api_key
    }
    url = base_url + endpoint
    response = requests.post(url, headers=headers, params=params)