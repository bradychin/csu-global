import tensorflow as tf
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import glob
from collections import defaultdict
from tensorflow import keras
from tensorflow.keras import layers

# Step 1: Load and preprocess the image data
print("Step 1: Loading and preprocessing image data...")

IMG_SIZE = (94, 125)

def pixels_from_path(file_path):
    im = Image.open(file_path)
    im = im.resize(IMG_SIZE)
    np_im = np.array(im)
    return np_im

# Check image shapes (commented out for assignment completion)
# shape_counts = defaultdict(int)
# for i, cat in enumerate(glob.glob('cats/*')[:1000]):
#     if i%100==0:
#         print(i)
#     img_shape = pixels_from_path(cat).shape
#     shape_counts[str(img_shape)]= shape_counts[str(img_shape)]+ 1

# shape_items = list(shape_counts.items())
# shape_items.sort(key = lambda x: x[1])
# shape_items.reverse()

# Load data
validation_size = 0.1
img_size = IMG_SIZE
num_channels = 3
SAMPLE_SIZE = 2048

print("loading training cat images...")
cat_train_set = np.asarray([pixels_from_path(cat) for cat in glob.glob('cats/*')[:SAMPLE_SIZE]])
print("loading training dog images...")
dog_train_set = np.asarray([pixels_from_path(dog) for dog in glob.glob('dogs/*')[:SAMPLE_SIZE]])

valid_size = 512
print("loading validation cat images...")
cat_valid_set = np.asarray([pixels_from_path(cat) for cat in glob.glob('cats/*')[-valid_size:]])
print("loading validation dog images...")
dog_valid_set = np.asarray([pixels_from_path(dog) for dog in glob.glob('dogs/*')[-valid_size:]])

# Combine training and validation data
x_train = np.concatenate([cat_train_set, dog_train_set])
labels_train = np.asarray([1 for _ in range(SAMPLE_SIZE)]+[0 for _ in range(SAMPLE_SIZE)])
x_valid = np.concatenate([cat_valid_set, dog_valid_set])
labels_valid = np.asarray([1 for _ in range(valid_size)]+[0 for _ in range(valid_size)])

# Normalize pixel values
x_train = x_train.astype('float32') / 255.0
x_valid = x_valid.astype('float32') / 255.0

print(f"Training data shape: {x_train.shape}")
print(f"Validation data shape: {x_valid.shape}")

# Initial simple model (single hidden layer)
print("\nStep 2: Training simple model with single hidden layer...")

total_pixels = img_size[0] * img_size[1] * 3
fc_size = 512

inputs = keras.Input(shape=(img_size[1], img_size[0], 3), name='ani_image')
x = layers.Flatten(name='flattened_img')(inputs)
x = layers.Dense(fc_size, activation='relu', name='first_layer')(x)
outputs = layers.Dense(1, activation='sigmoid', name='class')(x)

model = keras.Model(inputs=inputs, outputs=outputs)

# Step 2: Configure model with AdamOptimizer, MSE loss, 10 epochs
customAdam = keras.optimizers.Adam(learning_rate=0.001)
model.compile(optimizer=customAdam,
              loss="mean_squared_error",
              metrics=["binary_crossentropy", "mean_squared_error"])

print('# Fit model on training data')
history = model.fit(x_train,
                    labels_train,
                    batch_size=32,
                    shuffle=True,
                    epochs=10,  # Changed to 10 as requested
                    validation_data=(x_valid, labels_valid))

# Step 3: Train CNN with convolution layer
print("\nStep 3: Training CNN with convolution layer...")

fc_layer_size = 128
img_size = IMG_SIZE

conv_inputs = keras.Input(shape=(img_size[1], img_size[0], 3), name='ani_image')
conv_layer = layers.Conv2D(24, kernel_size=3, activation='relu')(conv_inputs)
conv_layer = layers.MaxPool2D(pool_size=(2, 2))(conv_layer)
conv_x = layers.Flatten(name='flattened_features')(conv_layer)

conv_x = layers.Dense(fc_layer_size, activation='relu', name='first_layer')(conv_x)
conv_x = layers.Dense(fc_layer_size, activation='relu', name='second_layer')(conv_x)
conv_outputs = layers.Dense(1, activation='sigmoid', name='class')(conv_x)

conv_model = keras.Model(inputs=conv_inputs, outputs=conv_outputs)

customAdam = keras.optimizers.Adam(learning_rate=1e-4)  # Adjusted learning rate
conv_model.compile(optimizer=customAdam,
                   loss="binary_crossentropy",
                   metrics=["binary_crossentropy", "mean_squared_error"])

print('# Fit CNN model on training data')
history_conv = conv_model.fit(x_train,
                              labels_train,
                              batch_size=32,
                              shuffle=True,
                              epochs=5,
                              validation_data=(x_valid, labels_valid))

# Calculate Pearson correlation
preds = conv_model.predict(x_valid)
preds = np.asarray([pred[0] for pred in preds])
correlation_coeff = np.corrcoef(preds, labels_valid)[0][1]
print(f"\nPearson correlation coefficient: {correlation_coeff}")

# Step 4: Analysis
print("\nStep 4: Analysis...")

# 1) Modified model with another convolutional layer and 48 kernels
print("1) Training model with additional convolutional layer...")

conv_inputs_2 = keras.Input(shape=(img_size[1], img_size[0], 3), name='ani_image')
conv_layer_2 = layers.Conv2D(24, kernel_size=3, activation='relu')(conv_inputs_2)
conv_layer_2 = layers.MaxPool2D(pool_size=(2, 2))(conv_layer_2)
conv_layer_2 = layers.Conv2D(48, kernel_size=3, activation='relu')(conv_layer_2)  # Additional layer
conv_layer_2 = layers.MaxPool2D(pool_size=(2, 2))(conv_layer_2)
conv_x_2 = layers.Flatten(name='flattened_features')(conv_layer_2)

conv_x_2 = layers.Dense(fc_layer_size, activation='relu', name='first_layer')(conv_x_2)
conv_x_2 = layers.Dense(fc_layer_size, activation='relu', name='second_layer')(conv_x_2)
conv_outputs_2 = layers.Dense(1, activation='sigmoid', name='class')(conv_x_2)

conv_model_2 = keras.Model(inputs=conv_inputs_2, outputs=conv_outputs_2)

customAdam_2 = keras.optimizers.Adam(learning_rate=1e-4)
conv_model_2.compile(optimizer=customAdam_2,
                     loss="binary_crossentropy",
                     metrics=["binary_crossentropy", "mean_squared_error"])

history_conv_2 = conv_model_2.fit(x_train,
                                  labels_train,
                                  batch_size=32,
                                  shuffle=True,
                                  epochs=5,
                                  validation_data=(x_valid, labels_valid))

preds_2 = conv_model_2.predict(x_valid)
preds_2 = np.asarray([pred[0] for pred in preds_2])
correlation_coeff_2 = np.corrcoef(preds_2, labels_valid)[0][1]
print(f"New correlation coefficient with additional conv layer: {correlation_coeff_2}")

# 2) Assess accuracy
print("\n2) Model accuracy assessment:")
predictions_binary = (preds > 0.5).astype(int)
accuracy = np.mean(predictions_binary == labels_valid)
print(f"Accuracy: {accuracy:.4f}")

# Create scatterplot
plt.figure(figsize=(8, 6))
sns.scatterplot(x=preds, y=labels_valid)
plt.xlabel('Predictions')
plt.ylabel('True Labels')
plt.title('Predictions vs True Labels')
plt.show()

# Threshold analysis
cat_quantity = sum(labels_valid)
print(f"\nTotal cats in validation set: {cat_quantity}")

for i in range(1, 10):
    threshold = 0.1 * i
    above_threshold = preds > threshold
    if np.sum(above_threshold) > 0:
        cat_ratio = sum(labels_valid[above_threshold]) / labels_valid[above_threshold].shape[0]
        print(f'threshold: {threshold:.1f} - Cat ratio: {cat_ratio:.4f}')

# Step 5: Utility functions
print("\nStep 5: Utility functions...")

def animal_pic(index):
    """Display image at given index"""
    return Image.fromarray((x_valid[index] * 255).astype(np.uint8))

def cat_probability(index):
    """Return probability of image being a cat"""
    return conv_model.predict(np.asarray([x_valid[index]]))[0][0]

# Step 6: Save the model
print("\nStep 6: Saving model...")
conv_model.save('conv_model_big')
print("Model saved as 'conv_model_big'")

# Step 7: Interface example
print("\nStep 7: Interface example...")

def show_prediction(index):
    """Show image and prediction for given index"""
    prob = cat_probability(index)
    print(f"Index {index}: Probability of being a cat: {prob:.6f}")
    img = animal_pic(index)
    img.show()  # This will open the image in default viewer
    return prob, img

# Example usage
example_index = 124
prob, img = show_prediction(example_index)

# Additional examples
print("\nAdditional examples:")
for test_index in [50, 100, 200, 300]:
    prob = cat_probability(test_index)
    actual = "Cat" if labels_valid[test_index] == 1 else "Dog"
    print(f"Index {test_index}: Probability of being a cat: {prob:.6f} (Actual: {actual})")

print("\nAssignment completed successfully!")
print(f"Final model correlation coefficient: {correlation_coeff:.6f}")
print(f"Enhanced model correlation coefficient: {correlation_coeff_2:.6f}")
print(f"Model accuracy: {accuracy:.4f}")