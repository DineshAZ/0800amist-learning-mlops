#Import Libraries
import pandas as pd

import pickle

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

# Use Pickle to dump the Model
with open('model/rental-prediction-model.pkl', 'wb') as f:
  pickle.dump(model,f)

# Root Mean Square Error and Score Checks
y_pred = model.predict(X_test)
root_mean_squared_error_score = root_mean_squared_error(y_test, y_pred)
r2_score_value = r2_score(y_test, y_pred)


print("Root Mean Squared Error for Built Model",root_mean_squared_error_score)
print("Accuary Score for Built Model",r2_score_value)
print("Traning of Model Completed, and Model is Ready to Use !!")
