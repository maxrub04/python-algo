from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
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