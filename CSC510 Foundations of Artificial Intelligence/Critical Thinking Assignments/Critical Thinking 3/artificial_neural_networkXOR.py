# 1. Import libraries
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt

# 2. Input and Output data
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])  # Input layer
y = np.array([[0], [1], [1], [0]])  # Output layer

# 3. Create the model
# use sequential to stack layers
model = tf.keras.Sequential([
    tf.keras.layers.Dense(8, activation='relu', input_shape=(2,)),  # Hidden layer with input shape
    tf.keras.layers.Dense(1, activation='sigmoid')  # Output layer
])

# 4. Compile the model
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# 5. Train the model (using all data for training)
history = model.fit(X, y, epochs=5000, verbose=2)

# 6. Make predictions
predictions = model.predict(X)

# 7. Print predictions
print(f"Predictions: \n{predictions}")

# 8. Plot the training loss values
plt.plot(history.history['loss'])
plt.title('Model Loss')
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.show()

# 9. Plot the training accuracy values
plt.plot(history.history['accuracy'])
plt.title('Model Accuracy')
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.show()