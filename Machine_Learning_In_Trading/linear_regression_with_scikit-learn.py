import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

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


# We use the previous values as indicators to predict the next price value
data["Target"] = data["Price"].shift(-1)
data = data.dropna()

# Define the attributes matrix and the target variable
X = data[["Price", "SMA_5"]]
y = data["Target"]

# Divide data into training and tests sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create and train a linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Predicting values for the test set
y_pred = model.predict(X_test)

# Calculating the error metrics
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("Mean Squared Error:", mse)
print("R² Score:", r2)

# Output the coefficients of the model
print("Regression coefficient:", model.coef_)
print("Baseline value:", model.intercept_)

import matplotlib.pyplot as plt
plt.figure(figsize=(10, 5))
plt.scatter(y_test, y_pred, color="blue", label="Predicted prices")
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], "r--", label="Ideal Line")
plt.xlabel("True Price")
plt.ylabel("Predicted Price")
plt.title("Linear Regression: True vs Predicted prices")
plt.legend()
plt.grid(True)
plt.show()