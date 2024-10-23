#Import Libraries
import pandas as pd
import numpy as np

import json
import pickle


# Use Pickle to dump the Model
with open('model/rental-prediction-model.pkl', 'rb') as f:
  model = pickle.load(f)

# Using Data as JSON File
with open('inputs/inputs.json', 'r') as f:
  user_input = json.load(f)

# User Entries Using JSON
rooms = user_input['rooms']
sqft = user_input['sqft']
user_input_prediction= np.array([[rooms,sqft]])

# print("No.of Rooms:",user_input['rooms'])
# print("Area in Sqft:",user_input['sqft'])

# Model Predicition
predicted_rental_price = model.predict(user_input_prediction)
output = {"Rental Prediction using Built Model": predicted_rental_price[0]}

with open('outputs/outputs.json', 'w') as f:
  json.dump(output, f)

print("####################################### Prediction Started Using Model #######################################")
print("Model Predicted and Results are uploaded to outputs")
print("####################################### Prediction Concluded Using Model #######################################")
