import pandas as pd
import numpy as np
from collections import Counter

# Step 1: Load the data
data = pd.read_csv('iris.csv')

# Step 2: Separate features and target
X = data.drop('Name', axis=1).values  # Features (all columns except the target)
y = data['Name'].values  # Target variable (species)

# Step 3: Initialize the value of k
k = 3  # You can change this value


# Function to calculate the Euclidean distance
def euclidean_distance(point1, point2):
    return np.sqrt(np.sum((point1 - point2) ** 2))


# Step 4: Function to predict the class of a test point
def predict(test_point, X_train, y_train, k):
    distances = []

    # Step 5: Iterate through all training data points and calculate distance
    for i in range(len(X_train)):
        dist = euclidean_distance(test_point, X_train[i])
        distances.append((dist, y_train[i]))

    # Step 6: Sort the distances in ascending order
    distances.sort(key=lambda x: x[0])

    # Step 7: Get top k rows from the sorted array
    k_neighbors = distances[:k]

    # Step 8: Get the most frequent class from these k neighbors
    class_votes = [neighbor[1] for neighbor in k_neighbors]
    most_common_class = Counter(class_votes).most_common(1)[0][0]

    return most_common_class


# Function to take user input for the test point
def get_user_input():
    print("Enter the following details for prediction (in floating point):")
    sepal_length = float(input("Sepal length: "))
    sepal_width = float(input("Sepal width: "))
    petal_length = float(input("Petal length: "))
    petal_width = float(input("Petal width: "))

    return np.array([sepal_length, sepal_width, petal_length, petal_width])


# Accept user input
test_point = get_user_input()

# Step 9: Predict the class for the input test point
predicted_class = predict(test_point, X, y, k)

print(f'Predicted class: {predicted_class}')