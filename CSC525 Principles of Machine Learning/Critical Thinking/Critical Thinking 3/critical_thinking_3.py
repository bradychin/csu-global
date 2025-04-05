from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
import pandas as pd

salary_data = pd.read_csv('Salary_Data.csv')
features = salary_data[['YearsExperience']]
target = salary_data[['Salary']]

# Polynomial feature transformation
poly = PolynomialFeatures(degree=4)
x_poly = poly.fit_transform(features)

# Train the model
model = LinearRegression()
model.fit(x_poly, target)

# Make prediction for a new data point
years_of_experience = 10
years_exp_poly = poly.transform(pd.DataFrame([[years_of_experience]], columns=features.columns))
predicted_salary = model.predict(years_exp_poly)

print(f'\nPredicted Salary after {years_of_experience} years of experience: ${predicted_salary[0][0]:.2f}\n')