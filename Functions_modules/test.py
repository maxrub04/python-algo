#import trading_tools
from trading_tools import calculate_loss
from trading_tools import calculate_profit

def calculate_profit(entry_price,exit_price):
    """
        Calculates the profit or loss of the transaction.

        Arguments:
                entry_price (float): The purchase price of the asset.
                exit_price (float): The selling price of the asset.

        Returns:
                float: Profit (if positive) or loss (if negative).
-
        Returns None if an error occurs.
        """
    try:
        result_price = exit_price - entry_price
    except ValueError:
        print("Wrong input")
        result_price = None

    return result_price

entry_price = float(input("Enter the price you wish to buy: "))
exit_price = float(input("Enter the price you wish to sell: "))
result1 = calculate_profit(entry_price, exit_price)
print("Your profit is:", result1)
result2 = calculate_loss(entry_price, exit_price)
print("Your loss is:", result2)