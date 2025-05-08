#pip install mplfinance

import requests
import pandas as pd
import mplfinance as mpf

# Data from Binance
url = "https://api.binance.com/api/v3/klines"
params = {
    "symbol": "BTCUSDT",
    "interval": "1h",
    "limit": 50  # last 50 candles
}
response = requests.get(url, params=params)
klines = response.json()

# Convert into DataFrame
df = pd.DataFrame(klines, columns=[
    "timestamp", "open", "high", "low", "close", "volume",
    "close_time", "quote_asset_volume", "number_of_trades",
    "taker_buy_base_volume", "taker_buy_quote_volume", "ignore"
])

# Convert types
df["timestamp"] = pd.to_datetime(df["timestamp"], unit="ms")
df.set_index("timestamp", inplace=True)
df[["open", "high", "low", "close", "volume"]] = df[["open", "high", "low", "close", "volume"]].astype(float)

# plotting
mpf.plot(df[["open", "high", "low", "close", "volume"]],
         type="candle", style="yahoo", volume=True, title="BTCUSDT 1h Candles")
