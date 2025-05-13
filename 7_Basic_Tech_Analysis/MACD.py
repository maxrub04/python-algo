import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#Moving Average Convergence Divergence)


dates = pd.date_range(start="2023-01-01", periods=30, freq="D")
prices = np.random.normal(loc=35000, scale=500, size=30)
df = pd.DataFrame({"Date": dates, "Price": prices})
df.set_index("Date", inplace=True)


