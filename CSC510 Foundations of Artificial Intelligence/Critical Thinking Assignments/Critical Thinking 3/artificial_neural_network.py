import numpy as np
# import tensorflow as tf
import tf_keras

# Input and Output data
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])  # Input layer
y = np.array([[0], [1], [1], [0]])  # Output layer

# Create the model
model = tf_keras.Sequential([
    tf_keras.layers.Dense(4, activation='relu', input_shape=(2,)),  # Hidden layer with input shape
    tf_keras.layers.Dense(1, activation='sigmoid')  # Output layer
])

# Compile the model
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Train the model
model.fit(X, y, epochs=5000, verbose=0)

# Make predictions
predictions = model.predict(X)

# Print predictions
print(f"Predictions: \n{predictions}")
