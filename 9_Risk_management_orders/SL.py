

def calculate_stop_loss(entry_price, risk_pct=0.03, method="fixed", support_level=None):
    """
    Calculates the stop loss level for the trade.
    Arguments:
    entry_price (float): Entry price.
    risk_pct (float): Allowable risk percentage (for fixed method).
    method (str): Stop loss calculation method ("fixed" or "support").
    support_level (float): Support level (required for the "support" method).
    Returns:
    float: Stop loss level.
    """
    if method == "fixed":
        return entry_price * (1 - risk_pct)
    elif method == "support" and support_level is not None:

    # Some clearance (buffer) can be added to increase reliability
        return support_level * 0.99 # 1% gap below the support level
    else:
        raise ValueError("Incorrect method or missing support level")


# example
entry_price = 35000
stop_loss_fixed = calculate_stop_loss(entry_price, risk_pct=0.03, method="fixed")
stop_loss_support = calculate_stop_loss(entry_price, method="support", support_level=34500)
print("Fixed stop loss:", stop_loss_fixed)
print("Stop loss at the support level:", stop_loss_support)