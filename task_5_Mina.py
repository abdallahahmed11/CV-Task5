import cv2
import os
# Function to detect faces in images
def detect_faces(image_path):
    # Load the pre-trained face cascade
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    # Read the image
    img = cv2.imread(image_path)
    # Convert the image to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Detect faces
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    # Draw rectangles around the detected faces
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
    return img
# Path to the ORL dataset directory
dataset_dir = "c:/Users/Mina A Tayeh/Desktop/CV task 5/ORL_dataset1"
# Loop through each person folder
for person_folder in os.listdir(dataset_dir):
    person_path = os.path.join(dataset_dir, person_folder)
    # Loop through each image in the person folder
    for image_file in os.listdir(person_path):
        image_path = os.path.join(person_path, image_file)
        # Detect faces in the image
        result_img = detect_faces(image_path)
        # Display the result
        cv2.imshow('Detected Faces', result_img)
        cv2.waitKey(1000)  # Show the image for 1 second
        cv2.destroyAllWindows()
