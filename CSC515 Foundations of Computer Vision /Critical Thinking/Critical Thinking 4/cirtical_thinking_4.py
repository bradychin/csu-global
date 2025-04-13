import cv2

image = cv2.imread('Mod4CTd1.jpg')
# try:
# except:
#     print('File does not exist')

cv2.imshow('Image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()

