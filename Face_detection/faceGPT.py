import cv2
import numpy as np
import keras
from cvzone.FaceDetectionModule import FaceDetector

# Load the pre-trained model
model = keras.models.load_model('fer2013_mini_XCEPTION.102-0.66.hdf5', compile=True)

# Face detector
detector = FaceDetector(minDetectionCon=0.5, modelSelection=1)

# Function to preprocess the frame
def preprocess_frame(frame, x, y, w, h):
    # Crop the face region
    face_roi = frame[y:y+h, x:x+w]
    # Resize to match model input size
    resized_face = cv2.resize(face_roi, (64, 64))
    # Convert to grayscale
    gray_face = cv2.cvtColor(resized_face, cv2.COLOR_BGR2GRAY)
    # Normalize pixel values
    normalized_face = gray_face / 255.0
    # Expand dimensions to match model input shape
    processed_face = np.expand_dims(np.expand_dims(normalized_face, axis=-1), axis=0)
    return processed_face

# Access the camera feed
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open camera.")
    exit()

while True:
    # Read frame from the camera
    success, img = cap.read()

    # Detect faces
    img, bboxs = detector.findFaces(img, draw=False)
    
    # Process each detected face
    if bboxs:
        # Loop through each bounding box
        for bbox in bboxs:
            # bbox contains 'id', 'bbox', 'score', 'center'

            # ---- Get Data  ---- #
            center = bbox["center"]
            x, y, w, h = bbox['bbox']
            score = int(bbox['score'][0] * 100)
    
            # Preprocess the face region
            processed_face = preprocess_frame(img, x, y, w, h)
        
            # Make predictions
            predictions = model.predict(processed_face)
        
            labels = ['angry', 'disgust', 'fear', 'happy', 'neutral', 'sad', 'surprise']

            # Assign the label based on predictions
            label = labels[np.argmax(predictions[0])]  

            # ---- Draw Data  ---- #
            cv2.circle(img, center, 5, (255, 0, 255), cv2.FILLED)
            cv2.putText(img, label, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36,255,12), 2)
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 255), 2)

    # Display the result
    cv2.imshow('Emotion Detection', img)
    
    # Exit on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close the OpenCV window
cap.release()
cv2.destroyAllWindows()
