"""
Instructions:

1. Unzip folder named 'unaugmented_dataset'.
2. Place unaugmented_dataset into the same folder as this script.
3. Run script
"""

import os
import random
from PIL import Image, ImageEnhance, ImageOps, ImageFilter
import numpy as np

# Define input and output directories
input_dir = "unaugmented_dataset"
output_dir = "augmented_dataset"

# Create output directory if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

def apply_augmentation(image):
    """Apply a random augmentation to the image."""
    # Choose a random augmentation
    augmentation_type = random.choice([
        'rotate', 'flip', 'color', 'contrast', 'brightness',
        'blur', 'crop_and_resize', 'noise'
    ])

    if augmentation_type == 'rotate':
        # Rotate by a random angle between -30 and 30 degrees
        angle = random.uniform(-30, 30)
        return image.rotate(angle, expand=True)

    elif augmentation_type == 'flip':
        # Horizontal flip
        return ImageOps.mirror(image)

    elif augmentation_type == 'color':
        # Adjust color balance
        factor = random.uniform(0.5, 1.5)
        enhancer = ImageEnhance.Color(image)
        return enhancer.enhance(factor)

    elif augmentation_type == 'contrast':
        # Adjust contrast
        factor = random.uniform(0.5, 1.5)
        enhancer = ImageEnhance.Contrast(image)
        return enhancer.enhance(factor)

    elif augmentation_type == 'brightness':
        # Adjust brightness
        factor = random.uniform(0.5, 1.5)
        enhancer = ImageEnhance.Brightness(image)
        return enhancer.enhance(factor)

    elif augmentation_type == 'blur':
        # Apply gaussian blur
        return image.filter(ImageFilter.GaussianBlur(radius=random.uniform(0.5, 2.0)))

    elif augmentation_type == 'crop_and_resize':
        # Random crop and resize back to original dimensions
        width, height = image.size
        crop_percent = random.uniform(0.8, 0.9)
        crop_width = int(width * crop_percent)
        crop_height = int(height * crop_percent)

        left = random.randint(0, max(0, width - crop_width))
        top = random.randint(0, max(0, height - crop_height))
        right = left + crop_width
        bottom = top + crop_height

        cropped = image.crop((left, top, right, bottom))
        return cropped.resize((width, height))

    elif augmentation_type == 'noise':
        # Add random noise
        img_array = np.array(image)
        noise = np.random.normal(0, 15, img_array.shape)
        noisy_img = np.clip(img_array + noise, 0, 255).astype(np.uint8)
        return Image.fromarray(noisy_img)


# Set number of augmentations per image
num_augmentations = 5

# Get all files in the input directory
image_files = [f for f in os.listdir(input_dir) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
print(f"Found {len(image_files)} images to augment.")

# Process each image
for filename in image_files:
    try:
        # Open image file
        img_path = os.path.join(input_dir, filename)
        with Image.open(img_path) as img:
            # Convert to RGB if necessary
            if img.mode != 'RGB':
                img = img.convert('RGB')

            # Copy original image to output directory
            original_save_path = os.path.join(output_dir, filename)
            img.save(original_save_path)

            # Generate augmented versions
            name, ext = os.path.splitext(filename)
            for i in range(num_augmentations):
                augmented_img = apply_augmentation(img.copy())
                aug_filename = f"{name}_aug_{i + 1}{ext}"
                save_path = os.path.join(output_dir, aug_filename)
                augmented_img.save(save_path)

        print(f"Processed: {filename}")

    except Exception as e:
        print(f"Error processing {filename}: {e}")

print(f"Augmentation complete. {len(image_files) * (num_augmentations + 1)} total images in output folder.")