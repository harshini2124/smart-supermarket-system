import pandas as pd
from sklearn.tree import DecisionTreeClassifier
import numpy as np

# Dummy training data
data = {
    "days_left": [1, 3, 5, 10, 15, 20],
    "stock": [30, 20, 25, 40, 50, 60],
    "discount": [3, 3, 2, 2, 1, 1]
}

df = pd.DataFrame(data)

X = df[["days_left", "stock"]]
y = df["discount"]

model = DecisionTreeClassifier()
model.fit(X, y)

def predict_discount(days_left, stock):
    """
    Returns discount level:
    1 -> 10%, 2 -> 20%, 3 -> 40%
    """
    X_test = np.array([[days_left, stock]])
    result = model.predict(X_test)
    return result[0]
