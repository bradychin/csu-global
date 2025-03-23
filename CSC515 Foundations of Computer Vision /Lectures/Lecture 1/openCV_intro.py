import cv2

img = cv2.imread('sunflower.jpg')
cv2.imwrite('sunflower_copy.jpg', img) # Creates copy
cv2.imshow('sunflower_window', img) # Displays window with title
cv2.waitKey(0) # Display until a key is pressed
cv2.destroyAllWindows() # Closes all opened windows


