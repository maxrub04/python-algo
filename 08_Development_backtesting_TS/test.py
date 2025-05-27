from backtesting import Strategy, Backtest
from backtesting.lib import crossover
from backtesting.test import SMA
import yfinance as yf
import pandas as pd


class SmaCross(Strategy):
    # Define the two MA lags as class variables
    # for later optimization
    n1 = 20  # faster SMA
    n2 = 40  # slower SMA

    def init(self):
        # Precompute the two moving averages
        self.sma1 = self.I(SMA, self.data.Close, self.n1)
        self.sma2 = self.I(SMA, self.data.Close, self.n2)

    def next(self):
        # If sma1 crosses above sma2, close any existing
        # short trades, and buy the asset
        if crossover(self.sma1, self.sma2):
            self.position.close()
            self.buy()

        # Else, if sma1 crosses below sma2, close any existing
        # long trades, and sell the asset
        elif crossover(self.sma2, self.sma1):
            self.position.close()
            self.sell()


# Download historical data
data = yf.download('AAPL', start='2023-01-01', end='2024-01-01')

# Create and run a backtest
bt = Backtest(data, SmaCross,
              cash=10000,  # Initial capital
              commission=.002)  # Commission 0.2%

# Run the backtest
stats = bt.run()

# Print results
print('\nBacktest Results:')
print('----------------')
print(f'Return: {stats["Return [%]"]:.2f}%')
print(f'Maximum Drawdown: {stats["Max. Drawdown [%]"]:.2f}%')
print(f'Sharpe Ratio: {stats["Sharpe Ratio"]:.2f}')
print(f'Number of Trades: {stats["# Trades"]}')

# Plot the backtest results
bt.plot()

# Optional: Parameter optimization
optimized_stats = bt.optimize(
    n1=range(10, 30, 5),  # First SMA from 10 to 30 with step 5
    n2=range(20, 50, 5),  # Second SMA from 20 to 50 with step 5
    maximize='Sharpe Ratio'  # Optimization criterion
)

# Print optimization results
print('\nOptimization Results:')
print('-------------------')
print(f'Best parameters: n1={optimized_stats._strategy.n1}, n2={optimized_stats._strategy.n2}')
print(f'Best Sharpe Ratio: {optimized_stats["Sharpe Ratio"]:.2f}')
print(f'Best Return: {optimized_stats["Return [%]"]:.2f}%')