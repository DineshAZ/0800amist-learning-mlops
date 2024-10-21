#Import Libraries
import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Load the Dataset
df = pd.read_csv('data/rental_1000.csv')

# Features and Labels
X = df[['rooms','sqft']].values  # Features
y = df['price'].values           # Label

#Split the data for Training and Testing
X_train, X_test, y_train, y_test = train_test_split(X, y,test_size=0.20,random_state=0)

# Build the model
lr = LinearRegression()
model = lr.fit(X_train, y_train)

# Predicted the values
predicted_rental_price = model.predict(np.array([X_test[0]]))

print("####################################### Prediction Started Using Model #######################################")
print(f"Actual Rental Price with Rooms: {X_test[0][0]} and Sqft + {X_test[0][1]} is {y_test[0]}")
print(f"Predicted Rental Price with Rooms: {X_test[0][0]} and Sqft + {X_test[0][1]} is {predicted_rental_price}")
print("####################################### Prediction Concluded Using Model #######################################")

