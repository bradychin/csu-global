import cv2
import numpy as np
import matplotlib.pyplot as plt

def mean_filter(image, kernel_size):
    return cv2.blur(image, (kernel_size, kernel_size))

def median_filter(image, kernel_size):
    return cv2.medianBlur(image, kernel_size)

def gaussian_filter(image, kernel_size, sigma):
    return cv2.GaussianBlur(image, (kernel_size, kernel_size), sigma)

def main():
    image = cv2.imread('Mod4CT1.jpg')

    figure, axes = plt.subplots(3, 4, figsize=(12, 8))

    kernel_sizes = [3,5,7]
    sigma_sizes = [0.5, 2.0]

    axes[0, 0].set_title(f'Mean Filter')
    axes[0, 1].set_title(f'Median Filter')
    axes[0, 2].set_title(f'Gaussian Filter Sigma {sigma_sizes[0]}')
    axes[0, 3].set_title(f'Gaussian Filter Sigma {sigma_sizes[1]}')

    for i, ksize in enumerate(kernel_sizes):
        figure.text(0.08, 0.75 - i * 0.25, f'{ksize}x{ksize} Kernel',
                    va='center', rotation=90, fontsize=12)

        mean = mean_filter(image, ksize)
        median = median_filter(image, ksize)
        gaussian0 = gaussian_filter(image, ksize, sigma_sizes[0])
        gaussian1 = gaussian_filter(image, ksize, sigma_sizes[1])

        axes[i, 0].imshow(mean)
        axes[i, 0].set_xticks([])
        axes[i, 0].set_yticks([])

        axes[i, 1].imshow(median)
        axes[i, 1].set_xticks([])
        axes[i, 1].set_yticks([])

        axes[i, 2].imshow(gaussian0)
        axes[i, 2].set_xticks([])
        axes[i, 2].set_yticks([])

        axes[i, 3].imshow(gaussian1)
        axes[i, 3].set_xticks([])
        axes[i, 3].set_yticks([])

    plt.show()

if __name__ == '__main__':
    main()