#Import Libraries
import pandas as pd
import numpy as np

import json

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import root_mean_squared_error
from sklearn.metrics import r2_score

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

# Root Mean Square Error and Score Checks
y_pred = model.predict(X_test)
root_mean_squared_error_score = root_mean_squared_error(y_test, y_pred)
r2_score_value = r2_score(y_test, y_pred)

# User Entries Using Inputs
#rooms = int(input("Enter the no.of rooms:"))
#sqft = int(input("Enter the area in Sqft:"))
#user_input = np.array([[rooms,sqft]])

# Using Data as JSON Entry
#data = '{"rooms": 2, "sqft": 1000 }'
#user_input = json.loads(data)

# Using Data as JSON File
with open('data/inputs.json', 'r') as f:
  user_input = json.load(f)

# User Entries Using JSON
rooms = user_input['rooms']
sqft = user_input['sqft']
user_input_prediction= np.array([[rooms,sqft]])

print("No.of Rooms:",user_input['rooms'])
print("Area in Sqft:",user_input['sqft'])

# Model Predicition
predicted_rental_price = model.predict(user_input_prediction)

print("####################################### Prediction Started Using Model #######################################")
print(f"Predicted Rental Price with Rooms={rooms} and Sqft={sqft} is {predicted_rental_price[0]:2f}")
print("####################################### Prediction Concluded Using Model #######################################")

print("Root Mean Squared Error for Built Model",root_mean_squared_error_score)
print("Accuary Score for Built Model",r2_score_value)


