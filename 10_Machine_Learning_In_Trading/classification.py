import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
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

data["Target"] = data["Price"].shift(-1)
data = data.dropna()

# Create a target variable for classification
data["Signal"] = (data["Target"] > data["Price"]).astype(int) # 1, if price rises, 0 if false
X = data[["Price", "SMA_5"]]
y = data["Signal"]
# Divide data into training and tests sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create and train a logistic regression model
clf = LogisticRegression()
clf.fit(X_train, y_train)
# Prediction on the test set
y_pred = clf.predict(X_test)
# Estimating the accuracy of the model
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)
print("Classification Report:")
print(classification_report(y_test, y_pred))

plt.figure(figsize=(10, 5))
plt.scatter(X_test["Price"], X_test["SMA_5"], c=y_pred, cmap="coolwarm", label="Classified signals")
plt.xlabel("Price")
plt.ylabel("SMA_5")
plt.title("Feature space and predicted trading signals")
plt.colorbar(label="Signal (0 = Sell, 1 = Buy)")
plt.grid(True)
plt.show()