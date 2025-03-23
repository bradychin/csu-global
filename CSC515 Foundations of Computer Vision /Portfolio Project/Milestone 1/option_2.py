"""
Instructions:

1. Ensure cv2 library is installed.
2. Place image "numbers.jpg" into the same folder as this python script.
3. Run script.
4. To close image, press any key.
"""

import cv2

image = cv2.imread('numbers.jpg') # read the image
cv2.imwrite('numbers_copy.jpg', image) # Creates copy of image in current folder
cv2.imshow('Numbers Image', image) # Disaply image
cv2.waitKey(0) # Display until a key is pressed
cv2.destroyAllWindows() # Closes all opened windows
