import cv2
import matplotlib.pyplot as plt

def morphological_operations(binary_image, kernel):
    dilated = cv2.dilate(binary_image, kernel, iterations=1)
    eroded = cv2.erode(binary_image, kernel, iterations=1)
    opened = cv2.morphologyEx(binary_image, cv2.MORPH_OPEN, kernel)
    closed = cv2.morphologyEx(binary_image, cv2.MORPH_CLOSE, kernel)

    return dilated, eroded, opened, closed

def main():
    image = cv2.imread('fingerprint.jpg', cv2.IMREAD_GRAYSCALE)

    threshold, binary_image = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))

    dilated, eroded, opened, closed = morphological_operations(binary_image, kernel)

    figure, axes = plt.subplots(2, 3, figsize=(12,8))

    axes[0, 0].imshow(image, cmap='gray')
    axes[0, 0].set_title('Original Image')

    axes[0, 1].imshow(binary_image, cmap='gray')
    axes[0, 1].set_title('Binary Image')

    axes[0, 2].imshow(dilated, cmap='gray')
    axes[0, 2].set_title('Dilated Image')

    axes[1, 0].imshow(eroded, cmap='gray')
    axes[1, 0].set_title('Eroded Image')

    axes[1, 1].imshow(opened, cmap='gray')
    axes[1, 1].set_title('Opened Image')

    axes[1, 2].imshow(closed, cmap='gray')
    axes[1, 2].set_title('Closed Image')

    plt.show()

if __name__ == '__main__':
    main()
