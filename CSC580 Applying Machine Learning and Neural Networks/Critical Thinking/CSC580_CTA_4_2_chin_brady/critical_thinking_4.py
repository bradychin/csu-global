import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt

# Generate synthetic data
N = 100
np.random.seed(0)
x_zeros = np.random.multivariate_normal(mean=[-1, -1], cov=0.1*np.eye(2), size=N//2)
y_zeros = np.zeros((N//2,))
x_ones = np.random.multivariate_normal(mean=[1, 1], cov=0.1*np.eye(2), size=N//2)
y_ones = np.ones((N//2,))

x_np = np.vstack([x_zeros, x_ones])
y_np = np.concatenate([y_zeros, y_ones])

# Plot data
plt.scatter(x_zeros[:, 0], x_zeros[:, 1], label='Class 0')
plt.scatter(x_ones[:, 0], x_ones[:, 1], label='Class 1')
plt.legend()
plt.title("Synthetic Data")
plt.show()

# Build logistic regression model using Keras
model = tf.keras.Sequential([
    tf.keras.layers.Dense(1, activation='sigmoid', input_shape=(2,))
])

model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=0.01),
              loss='binary_crossentropy',
              metrics=['accuracy'])

# Train model
history = model.fit(x_np, y_np, epochs=50, batch_size=16, verbose=0)

# Predict probabilities and classes
y_prob = model.predict(x_np).flatten()
y_pred = (y_prob >= 0.5).astype(int)

# Plot data with predicted classes
plt.scatter(x_np[:, 0], x_np[:, 1], c=y_pred, cmap='bwr', alpha=0.7)
plt.title("Predicted Classes")
plt.show()