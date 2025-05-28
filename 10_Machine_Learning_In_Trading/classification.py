from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
# Create a target variable for classification
data["Signal"] = (data["Target"] > data["Price"]).astype(int) # 1, if price rises, 0 if false
X = data[["Price", "SMA_5"]]
y = data["Signal"]
# Divide data into training and tests sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)