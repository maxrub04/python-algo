import matplotlib.pyplot as plt

days = [1, 2, 3, 4, 5]
price_asset1 = [34000, 35200, 35100, 35300, 35500]
price_asset2 = [2700, 2210, 5090, 2220, 2230]
plt.figure(figsize=(8, 5))
plt.plot(days, price_asset1, marker="o", linestyle="-", label="Asset 1", color="blue")
plt.plot(days, price_asset2, marker="s", linestyle="--", label="Asset 2", color="red")
plt.title("Price comparison by day")
plt.xlabel("Day")
plt.ylabel("Price")
plt.legend() # adding legend
plt.annotate("Trend Crossing", xy=(3, 35100), xytext=(3, 36000),
arrowprops=dict(facecolor="black", shrink=0.05))
plt.show()

# Applying the “ggplot” style for a cleaner appearance
plt.style.use("ggplot")
plt.figure(figsize=(8, 4))
plt.plot(days, price_asset1, marker="o", linestyle="-", color="green")
plt.title("Example of ggplot")
plt.xlabel("Day")
plt.ylabel("Price")
plt.show()