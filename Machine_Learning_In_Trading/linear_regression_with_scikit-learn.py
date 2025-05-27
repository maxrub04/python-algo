import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Generate an artificial DataFrame with historical data
np.random.seed(42)
dates = pd.date_range(start="2021-01-01", periods=100)
price = np.linspace(30000, 40000, 100) + np.random.normal(0, 500, 100)
sma = pd.Series(price).rolling(window=5, min_periods=1).mean().values
data = pd.DataFrame({
    "Date": dates,
    "Price": price,
    "SMA_5": sma
})
data.set_index("Date", inplace=True)

