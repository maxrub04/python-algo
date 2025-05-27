


# Position Size = (Capital * Risk per trade) / (Entry Price - Stop Loss)

capital = 100000
risk_per_trade = 0.02
dollar_risk = capital * risk_per_trade # 2000 USD
entry_price = 35000
stop_loss_price = 34300
risk_per_unit = entry_price - stop_loss_price # 700 USD

position_size = dollar_risk / risk_per_unit
print("Position size (in asset units):", position_size)