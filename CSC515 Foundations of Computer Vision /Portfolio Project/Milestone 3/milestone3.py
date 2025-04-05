"""
Instructions:

1. Ensure cv2 library is installed.
2. Place image "face_picture.png" into the same folder as this python script.
3. Run script.
4. To close image, press any key.
"""

import cv2

image = cv2.imread('face_picture.png')

cv2.rectangle(image, (246,352), (355,435), (0,0,255), 3) # Left eye
cv2.rectangle(image, (394,352), (513,435), (0,0,255), 3) # Right eye
cv2.circle(image, (381,369), 300, (0,255,0), 3) # Face
cv2.putText(image, 'this is me', (466,792), cv2.FONT_HERSHEY_PLAIN, 2, (255,255,255), 2)

cv2.imshow('This is me', image)
cv2.waitKey(0)
cv2.destroyAllWindows()