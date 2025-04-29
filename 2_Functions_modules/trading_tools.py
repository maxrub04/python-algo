def calculate_profit(entry_price,exit_price):
    try:
        result = exit_price - entry_price
    except TypeError:
        print("Error. Wrong entry/exit price.")
        result = None

    return result


def calculate_loss(entry_price, exit_price):
    try:
        result = exit_price - entry_price
    except TypeError:
        print("Error. Wrong entry/exit price.")
        result = None

    return result
