import numpy as np

# 1. Define input data (modify data if necessary)
x = np.array([[1],[3],[5],[7]])
y = np.array([[3],[5],[7],[9]])

# 2. Define weights and biases
# Xavier Initialization for weights
w1 = np.random.randn(x.shape[1], 3) * np.sqrt(2. / (x.shape[1] + 3))
w2 = np.random.randn(3, 1) * np.sqrt(2. / (3 + 1))

# Initialize biases to zeros or small values
b1 = np.zeros((1, 3))
b2 = np.zeros((1, 1))

# Activation function
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

epochs = 2000
learning_rate = 0.01

for epoch in range(epochs):
    # 3. Feedforward pass
    # Compute hidden layer
    z1 = np.dot(x, w1) + b1
    a1 = sigmoid(z1)
    # output layer
    y_pred = np.dot(a1,w2) + b2

    # 4. Calculate loss
    loss = np.mean((y-y_pred)**2)
    print(f'Epoch: {epoch+1} -> y_pred: {y_pred} Loss: {loss}')

    # 5. Backpropagation
    # Output layer gradient
    output_layer_error_term = y_pred-y
    # Hidden layer gradient
    hidden_layer_derivative = sigmoid(z1) * (1-sigmoid(z1))
    hidden_layer_error_term = np.dot(output_layer_error_term, w2.T) * hidden_layer_derivative
    # Update weights and biases
    output_layer_gradient_weights = np.dot(a1.T, output_layer_error_term)
    w2 = w2 - learning_rate * output_layer_gradient_weights
    b2 = b2 - learning_rate * np.sum(output_layer_error_term, axis=0, keepdims=True)
    hidden_layer_gradient_weights = np.dot(x.T, hidden_layer_error_term)
    w1 = w1 - learning_rate * hidden_layer_gradient_weights
    b1 = b1 - learning_rate * np.sum(hidden_layer_error_term, axis=0, keepdims=True)

print(f'\n\nPredicted Values:\n{y_pred}')