import cv2
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import precision_score, recall_score, f1_score


def create_synthetic_image(noise_std=0, obj_intensity=200, bg_intensity=50):
    img = np.full((256, 256), bg_intensity, dtype=np.uint8)
    cv2.rectangle(img, (60, 60), (120, 120), obj_intensity, -1)
    cv2.circle(img, (180, 180), 30, obj_intensity, -1)
    if noise_std > 0:
        noise = np.random.normal(0, noise_std, img.shape).astype(np.int16)
        img = np.clip(img.astype(np.int16) + noise, 0, 255).astype(np.uint8)
    return img


def generate_ground_truth():
    gt = np.zeros((256, 256), dtype=np.uint8)
    cv2.rectangle(gt, (60, 60), (120, 120), 255, 1)
    cv2.circle(gt, (180, 180), 30, 255, 1)
    return gt


def evaluate_metrics(detected_edges, ground_truth):
    gt_flat = (ground_truth.flatten() > 0).astype(np.uint8)
    det_flat = (detected_edges.flatten() > 0).astype(np.uint8)
    precision = precision_score(gt_flat, det_flat)
    recall = recall_score(gt_flat, det_flat)
    f1 = f1_score(gt_flat, det_flat)
    return precision, recall, f1


def run_edge_detectors(img, ground_truth, canny_thresh=(100, 200)):
    results = {}

    # Canny
    canny_edges = cv2.Canny(img, canny_thresh[0], canny_thresh[1])
    p, r, f1 = evaluate_metrics(canny_edges, ground_truth)
    results['Canny'] = (p, r, f1)

    # Sobel
    sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=3)
    sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=3)
    sobel_edges = cv2.magnitude(sobelx, sobely)
    sobel_edges = np.uint8(np.clip(sobel_edges, 0, 255))
    _, sobel_edges = cv2.threshold(sobel_edges, 50, 255, cv2.THRESH_BINARY)
    p, r, f1 = evaluate_metrics(sobel_edges, ground_truth)
    results['Sobel'] = (p, r, f1)

    # Laplacian
    laplacian = cv2.Laplacian(img, cv2.CV_64F)
    laplacian_edges = np.uint8(np.clip(np.abs(laplacian), 0, 255))
    _, laplacian_edges = cv2.threshold(laplacian_edges, 30, 255, cv2.THRESH_BINARY)
    p, r, f1 = evaluate_metrics(laplacian_edges, ground_truth)
    results['Laplacian'] = (p, r, f1)

    return results, canny_edges, sobel_edges, laplacian_edges


def show_all_images(original, noisy, intensity,
                    results_original, results_noisy, results_intensity):
    images = [
        original,
        results_original[0],
        results_original[1],
        results_original[2],
        noisy,
        results_noisy[0],
        results_noisy[1],
        results_noisy[2],
        intensity,
        results_intensity[0],
        results_intensity[1],
        results_intensity[2]
    ]

    titles = [
        'Original Image', 'Canny', 'Sobel', 'Laplacian',
        'Noisy Image', 'Canny', 'Sobel', 'Laplacian',
        'Noisy + Intensity', 'Canny', 'Sobel', 'Laplacian'
    ]

    plt.figure(figsize=(16, 9))
    for i in range(12):
        plt.subplot(3, 4, i+1)
        plt.imshow(images[i], cmap='gray')
        plt.title(titles[i], fontsize=10)
        plt.axis('off')
    plt.tight_layout()
    plt.show()


# --- Main Experiment ---

# Ground truth mask
gt = generate_ground_truth()

# Baseline image
img = create_synthetic_image()
results_orig, canny_orig, sobel_orig, laplacian_orig = run_edge_detectors(img, gt)
print("Original Image Metrics:")
for method, (p, r, f1) in results_orig.items():
    print(f"{method}: Precision={p:.3f}, Recall={r:.3f}, F1-Score={f1:.3f}")

# Noisy image
img_noisy = create_synthetic_image(noise_std=20)
results_noisy, canny_noisy, sobel_noisy, laplacian_noisy = run_edge_detectors(img_noisy, gt)
print("\nNoisy Image Metrics:")
for method, (p, r, f1) in results_noisy.items():
    print(f"{method}: Precision={p:.3f}, Recall={r:.3f}, F1-Score={f1:.3f}")

# Intensity + Noisy image
img_intensity = create_synthetic_image(noise_std=20, obj_intensity=150, bg_intensity=70)
results_intensity, canny_intensity, sobel_intensity, laplacian_intensity = run_edge_detectors(img_intensity, gt)
print("\nNoisy + Intensity Change Metrics:")
for method, (p, r, f1) in results_intensity.items():
    print(f"{method}: Precision={p:.3f}, Recall={r:.3f}, F1-Score={f1:.3f}")

# Show all images
show_all_images(
    img,
    img_noisy,
    img_intensity,
    (canny_orig, sobel_orig, laplacian_orig),
    (canny_noisy, sobel_noisy, laplacian_noisy),
    (canny_intensity, sobel_intensity, laplacian_intensity)
)