import cv2
import matplotlib.pyplot as plt

# Load classifiers
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

def preprocess_image(img):
    processed_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    processed_image = cv2.equalizeHist(processed_image)
    processed_image = cv2.bilateralFilter(processed_image, 9, 75, 75)
    return processed_image


def detect_faces(img, gray):
    faces = face_cascade.detectMultiScale(gray,
                                          scaleFactor=1.2,
                                          minNeighbors=4,
                                          minSize=(30,30))
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)
    return faces

def align_and_blur_eyes(img, face_coords):
    for (x, y, w, h) in face_coords:
        face = img[y:y + h, x:x + w]
        gray_face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
        eyes = eye_cascade.detectMultiScale(gray_face,
                                            scaleFactor=1.03,
                                            minNeighbors=1,
                                            minSize=(10,10))
        for (ex, ey, ew, eh) in eyes:
            eye_region = face[ey:ey + eh, ex:ex + ew]
            blurred = cv2.GaussianBlur(eye_region, (23, 23), 30)
            face[ey:ey + eh, ex:ex + ew] = blurred
        img[y:y + h, x:x + w] = face
    return img

def main():
    image_paths = [
        'images/full_body.jpg',
        'images/front_facing.jpeg',
        'images/front_facing_with_dog.jpg',
        'images/multiple_people.jpg',
        'images/person_far_away.jpg'
    ]

    results = []
    titles = ['Full Body', 'Front Facing', 'Front Facing with Dog', 'Multiple People', 'Far Away']

    for path in image_paths:
        img = cv2.imread(path)
        processed_image = preprocess_image(img)
        faces = detect_faces(img, processed_image)
        img = align_and_blur_eyes(img, faces)
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        results.append(img_rgb)

    for i in range(5):
        plt.subplot(2, 3, i+1)
        plt.imshow(results[i])
        plt.title(titles[i])
        plt.axis('off')

    plt.tight_layout()
    plt.show()

if __name__ == '__main__':
    main()