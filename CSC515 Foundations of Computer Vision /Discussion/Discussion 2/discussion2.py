import cv2
import numpy as np

# Load the image
image = cv2.imread("banknotes.jpg")  # Replace with your image path
if image is None:
    raise ValueError("Image not found. Check the file path.")

# Get image dimensions
(h, w) = image.shape[:2]

# 1. Translation (Shifting)
tx, ty = 25, 25  # Shift right by 50 pixels and down by 50 pixels
translation_matrix = np.float32([[1, 0, tx], [0, 1, ty]])
transformed = cv2.warpAffine(image, translation_matrix, (w, h))

# 2. Rotation (Aligning banknotes)
angle = -5  # Adjust based on the skew of the notes
center = (w // 2, h // 2)
rotation_matrix = cv2.getRotationMatrix2D(center, angle, 1.0)
transformed = cv2.warpAffine(transformed, rotation_matrix, (w, h))

# 3. Scaling (Standardizing size)
scale_x, scale_y = 1.2, 1.2  # 20% enlargement
new_w, new_h = int(w * scale_x), int(h * scale_y)

# Adjust transformation matrix to scale AND reposition the image
scaling_matrix = np.array([[scale_x, 0, (1 - scale_x) * w / 2],
                           [0, scale_y, (1 - scale_y) * h / 2]], dtype=np.float32)

transformed = cv2.warpAffine(transformed, scaling_matrix, (new_w, new_h))

# 4. Perspective Transformation (Fixing skew)
pts1 = np.float32([[100, 100], [w - 100, 100], [100, h - 100], [w - 100, h - 100]])
pts2 = np.float32([[90, 120], [w - 110, 100], [110, h - 90], [w - 90, h - 120]])
perspective_matrix = cv2.getPerspectiveTransform(pts1, pts2)
transformed = cv2.warpPerspective(transformed, perspective_matrix, (new_w, new_h))

# Show final transformed image
cv2.imshow("Transformed Image", transformed)
cv2.waitKey(0)
cv2.destroyAllWindows()