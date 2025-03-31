"""
Instructions:

1. Install cv2 and numpy libraries
2. Ensure the puppy image is in the same folder as this script
3. Ensure the puppy image is name 'puppy.jpg'
4. Run script
"""

import cv2
import numpy as np

img = cv2.imread('puppy.jpg')
print(img.shape)

blue_channel = img[:,:,0]
green_channel = img[:,:,1]
red_channel = img[:,:,2]
image_channels = np.hstack([blue_channel, green_channel, red_channel])

restored_image = cv2.merge([blue_channel, green_channel, red_channel])

swap_out_red = cv2.merge([blue_channel, green_channel, green_channel])

cv2.imshow('Original Image', img)
cv2.imshow('Image Channels', image_channels)
cv2.imshow('Restored Image', restored_image)
cv2.imshow('Red Green Swap', swap_out_red)

cv2.waitKey(0) # Display until a key is pressed
cv2.destroyAllWindows() # Closes all opened windows
