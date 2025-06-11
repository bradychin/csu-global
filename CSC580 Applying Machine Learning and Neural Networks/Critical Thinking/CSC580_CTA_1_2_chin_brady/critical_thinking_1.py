from random import randint
from sklearn.linear_model import LinearRegression

# Get number of variables
num_vars = int(input("Enter number of variables (4-8): "))
if num_vars < 4 or num_vars > 8:
    raise ValueError("Invalid number of variables.")

# Get coefficients
coefficients = []
for i in range(num_vars):
    coef = float(input(f"Enter coefficient for x{i+1}: "))
    coefficients.append(coef)

# Generate training data
TRAIN_SET_LIMIT = 1000
TRAIN_SET_COUNT = 500

TRAIN_INPUT = []
TRAIN_OUTPUT = []

for _ in range(TRAIN_SET_COUNT):
    inputs = [randint(0, TRAIN_SET_LIMIT) for _ in range(num_vars)]
    output = sum(c * x for c, x in zip(coefficients, inputs))
    TRAIN_INPUT.append(inputs)
    TRAIN_OUTPUT.append(output)

# Train model
model = LinearRegression()
model.fit(X=TRAIN_INPUT, y=TRAIN_OUTPUT)

# Test input
test_input = []
for i in range(num_vars):
    val = float(input(f"Enter test value for x{i+1}: "))
    test_input.append(val)

# Predict and compare
predicted = model.predict([test_input])[0]
actual = sum(c * x for c, x in zip(coefficients, test_input))

print(f"\nPredicted Value : {predicted}")
print(f"Actual Value    : {actual}")
print(f"Model Coefficients : {model.coef_}")