import cv2

img = cv2.imread('../../Critical Thinking/Critical Thinking 4/Mod4CT1.jpg')
cv2.imwrite('sunflower_copy.jpg', img) # Creates copy
cv2.imshow('sunflower_window', img) # Displays window with title
cv2.waitKey(0) # Display until a key is pressed
cv2.destroyAllWindows() # Closes all opened windows


# import cv2
# import urllib.request
# import numpy as np
#
# req = urllib.request.urlopen('https://csuglobal.instructure.com/courses/108108/files/7920365?wrap=1')
# arr = np.asarray(bytearray(req.read()), dtype=np.uint8)
# img = cv2.imdecode(arr, -1) # 'Load it as it is'
#
# cv2.imshow('random_title', img)
# if cv2.waitKey() & 0xff == 27: quit()