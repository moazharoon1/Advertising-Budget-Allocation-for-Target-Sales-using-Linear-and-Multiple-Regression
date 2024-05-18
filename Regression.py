import pandas as pd
import statsmodels.api as sm
import numpy as np

# Load the data
data = pd.read_csv('Advertising.csv')

# Define the target sales
target_sales = 300
budget = 1000

# Function to perform linear regression
def linear_regression(X, y):
    X = sm.add_constant(X)  # Adds a constant term to the predictor
    model = sm.OLS(y, X).fit()
    return model

# Function to perform multiple regression
def multiple_regression(X, y):
    X = sm.add_constant(X)  # Adds a constant term to the predictor
    model = sm.OLS(y, X).fit()
    return model

# Perform linear regression for each advertising medium
results = {}
for medium in ['TV', 'radio', 'newspaper']:
    X = data[[medium]]
    y = data['sales']
    model = linear_regression(X, y)
    results[medium] = model

# Perform multiple regression using all mediums
X_multiple = data[['TV', 'radio', 'newspaper']]
y = data['sales']
multiple_model = multiple_regression(X_multiple, y)

# Print the summary of each model
print("Linear Regression Results:")
for medium, model in results.items():
    print(f"\n{medium} model summary:")
    print(model.summary())

print("\nMultiple Regression Results:")
print(multiple_model.summary())

# Calculate required spending
coefficients = multiple_model.params
total_budget = 1000

# Calculate the sum of coefficients (excluding the intercept)
coeff_sum = coefficients[1:].sum()

# Calculate the proportion of the budget for each medium
proportions = coefficients[1:] / coeff_sum

# Calculate the spending for each medium
spending = proportions * total_budget

# Print the spending distribution
print("\nRequired spending distribution to achieve target sales:")
print(spending)

