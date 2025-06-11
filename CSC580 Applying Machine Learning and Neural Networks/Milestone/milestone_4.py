# Install dependencies if needed (uncomment on Colab)
# !pip install seaborn tensorflow tensorflow-docs

from __future__ import absolute_import, division, print_function, unicode_literals

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers

import tensorflow_docs as tfdocs
import tensorflow_docs.plots
import tensorflow_docs.modeling

# Download dataset
dataset_path = keras.utils.get_file(
    "auto-mpg.data",
    "http://archive.ics.uci.edu/ml/machine-learning-databases/auto-mpg/auto-mpg.data"
)

# Column names and import data
column_names = ['MPG','Cylinders','Displacement','Horsepower','Weight',
                'Acceleration', 'Model Year', 'Origin']

raw_dataset = pd.read_csv(dataset_path, names=column_names,
                          na_values = "?", comment='\t',
                          sep=" ", skipinitialspace=True)

dataset = raw_dataset.copy()

# Drop NA values
dataset = dataset.dropna()

# Split dataset
train_dataset = dataset.sample(frac=0.8, random_state=0)
test_dataset = dataset.drop(train_dataset.index)

# Separate labels
train_labels = train_dataset.pop('MPG')
test_labels = test_dataset.pop('MPG')

# Normalize data
train_stats = train_dataset.describe()
train_stats.pop("MPG")
train_stats = train_stats.transpose()

def norm(x):
    return (x - train_stats['mean']) / train_stats['std']

normed_train_data = norm(train_dataset)
normed_test_data = norm(test_dataset)

# Build model
def build_model():
    model = keras.Sequential([
        layers.Dense(64, activation='relu', input_shape=[len(train_dataset.keys())]),
        layers.Dense(64, activation='relu'),
        layers.Dense(1)
    ])
    optimizer = tf.keras.optimizers.RMSprop(0.001)
    model.compile(loss='mse', optimizer=optimizer, metrics=['mae', 'mse'])
    return model

model = build_model()

# Early stopping callback
early_stop = keras.callbacks.EarlyStopping(monitor='val_loss', patience=10)

# Train model
EPOCHS = 1000
early_history = model.fit(
    normed_train_data, train_labels,
    epochs=EPOCHS, validation_split=0.2, verbose=0,
    callbacks=[early_stop, tfdocs.modeling.EpochDots()]
)

# Plot training history (MAE)
plotter = tfdocs.plots.HistoryPlotter(smoothing_std=2)
plt.figure()
plotter.plot({'Early Stopping': early_history}, metric="mae")
plt.ylim([0, 10])
plt.ylabel('MAE [MPG]')
plt.title('Training History (MAE)')
plt.show()

# Evaluate on test set
loss, mae, mse = model.evaluate(normed_test_data, test_labels, verbose=2)
print(f"\nTesting set Mean Absolute Error: {mae:.2f} MPG")

# Predictions vs True
test_predictions = model.predict(normed_test_data).flatten()

plt.figure()
a = plt.axes(aspect='equal')
plt.scatter(test_labels, test_predictions)
plt.xlabel('True Values [MPG]')
plt.ylabel('Predictions [MPG]')
lims = [0, 50]
plt.xlim(lims)
plt.ylim(lims)
plt.plot(lims, lims)
plt.title('True vs Predicted MPG')
plt.show()

# Error distribution
error = test_predictions - test_labels
plt.figure()
plt.hist(error, bins=25)
plt.xlabel("Prediction Error [MPG]")
plt.ylabel("Count")
plt.title("Prediction Error Distribution")
plt.show()