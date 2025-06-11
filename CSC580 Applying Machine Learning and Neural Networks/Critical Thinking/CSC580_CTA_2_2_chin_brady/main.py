import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential, load_model
from keras.layers import Dense

# Load data
training_data_df = pd.read_csv("sales_data_training.csv")
test_data_df = pd.read_csv("sales_data_test.csv")

# Scale data
scaler = MinMaxScaler(feature_range=(0, 1))
scaled_training = scaler.fit_transform(training_data_df)
scaled_testing = scaler.transform(test_data_df)

scale_factor = scaler.scale_[8]
scale_min = scaler.min_[8]
print("Note: total_earnings values were scaled by multiplying by {:.10f} and adding {:.6f}".format(scale_factor, scale_min))

scaled_training_df = pd.DataFrame(scaled_training, columns=training_data_df.columns.values)
scaled_testing_df = pd.DataFrame(scaled_testing, columns=test_data_df.columns.values)

# Split inputs and outputs
X_train = scaled_training_df.drop('total_earnings', axis=1).values
Y_train = scaled_training_df[['total_earnings']].values
X_test = scaled_testing_df.drop('total_earnings', axis=1).values
Y_test = scaled_testing_df[['total_earnings']].values

# Build model
model = Sequential()
model.add(Dense(50, input_dim=9, activation='relu'))
model.add(Dense(25, activation='relu'))
model.add(Dense(1, activation='linear'))

model.compile(loss='mean_squared_error', optimizer='adam')

# Train model
model.fit(X_train, Y_train, epochs=50, shuffle=True, verbose=2)

# Evaluate model
test_error_rate = model.evaluate(X_test, Y_test, verbose=0)

# Save model
model.save("trained_model.h5")
print("Model saved to disk.")

# Load model & predict new product
model = load_model("trained_model.h5")
new_product_data = pd.read_csv("proposed_new_product.csv", header=None).values
prediction = model.predict(new_product_data)[0][0]

# Rescale prediction back to dollars
prediction = (prediction - scale_min) / scale_factor

# Print results
print(f"\nThe mean squared error (MSE) for the test data set is: {test_error_rate}")
print("Earnings Prediction for Proposed Product - ${:.2f}".format(prediction))