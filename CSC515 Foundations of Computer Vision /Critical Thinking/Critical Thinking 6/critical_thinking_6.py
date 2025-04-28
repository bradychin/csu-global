import cv2
import matplotlib.pyplot as plt

def load_images():
    indoor_scene = cv2.imread('indoor_scene.jpg', cv2.IMREAD_GRAYSCALE)
    outdoor_scene = cv2.imread('outdoor_scene.jpg', cv2.IMREAD_GRAYSCALE)
    close_up_scene = cv2.imread('close-up_scene.jpg', cv2.IMREAD_GRAYSCALE)
    return [indoor_scene, outdoor_scene, close_up_scene]

def adaptive_thresholding(scenes):
    processed_results = []
    block_size = 21
    c = 3
    for scene in scenes:
        gaussian_image = cv2.adaptiveThreshold(scene, 255,
                                                cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                                cv2.THRESH_BINARY, block_size, c)
        processed_results.append(gaussian_image)

    for scene in scenes:
        mean_image = cv2.adaptiveThreshold(scene, 255,
                                           cv2.ADAPTIVE_THRESH_MEAN_C,
                                           cv2.THRESH_BINARY, block_size, c)
        processed_results.append(mean_image)
    return processed_results

def display_results(images):
    titles = ['Indoor', 'Outdoor', 'Close-up',
              'Indoor Gaussian', 'Outdoor Gaussian', 'Close-up Gaussian',
              'Indoor Mean', 'Outdoor Mean', 'Close-up Mean']
    for i in range(len(images)):
        plt.subplot(3, 3, i+1)
        plt.imshow(images[i], cmap='gray')
        plt.title(titles[i])
        plt.axis('off')

    plt.tight_layout()
    plt.show()

def main():
    scenes = load_images()
    processed_results = adaptive_thresholding(scenes)
    images = scenes + processed_results
    display_results(images)

if __name__ == '__main__':
    main()