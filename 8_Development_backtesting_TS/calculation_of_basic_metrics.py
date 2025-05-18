import numpy as np
import pandas as pd


dates = pd.date_range(start="2021-01-01", periods=250)
equity = np.linspace(100000, 120000, 250)
df_equity = pd.DataFrame({"Date": dates, "Capital": equity})
df_equity.set_index("Date", inplace=True)



# Calculation of basic metrics
df_equity["Profitablity"] = df_equity["Capital"].pct_change()

# Sum of Profitablity
total_return = (df_equity["Capital"][-1] / df_equity["Capital"][0]) - 1

# Max Drowdown
rolling_max = df_equity["Capital"].cummax()
drawdown = (df_equity["Capital"] - rolling_max) / rolling_max
max_drawdown = drawdown.min()


# Sharpe Ratio
risk_free_rate = 0.01
daily_risk_free = risk_free_rate / 252
excess_return = df_equity["Profitablity"] - daily_risk_free
sharpe_ratio = np.sqrt(252) * excess_return.mean() / excess_return.std()

print("Sum of Profitablity: {:.2%}".format(total_return))
print("Max Drowdown: {:.2%}".format(max_drawdown))
print("Sharpe Ratio: {:.2f}".format(sharpe_ratio))