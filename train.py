import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import pickle

# Load dataset
df = pd.read_csv("https://raw.githubusercontent.com/azonecloud/mlapp-predict-rental/master/data/rental_1000.csv")

# Prepare Data
X = df[['rooms', 'sqft']].values  # Features - rooms and sqft
y = df['price'].values            # Label - price

# Split Data for Training and Testing
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)    

# Model Training
model = LinearRegression().fit(X_train, y_train) # Train the model


# Predict on a single example from the test set
predicted_rental = model.predict(X_test[0].reshape(1, -1))[0]

print("########################################### Testing Data Rental Price Prediction ###########################################")
print(f"Actual Rental Price for Property with rooms={X_test[0][0]} and Area Sqft={X_test[0][1]} is {y_test[0]}")
print(f"Predicted Rental Price for Property with rooms={X_test[0][0]} and Area Sqft={X_test[0][1]} is {predicted_rental}")
print("Pipeline Version V1 Release Completed")
print("########################################### Testing Data Rental Price Prediction ###########################################")
