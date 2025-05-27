




#Risk-Reward Ratio = (Target Price - Entry Price) / (Entry Price - Stop Loss)

entry_price = 35000
target_price = 36500
stop_loss_price = 34300
reward = target_price - entry_price # 1500 USD
risk = entry_price - stop_loss_price # 700 USD
risk_reward_ratio = reward / risk
print("Risk-Reward Ratio:", risk_reward_ratio)