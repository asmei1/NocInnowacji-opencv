# Simple test which take input from your camera
import numpy as np
import cv2

# Load the cascade
face_cascade = cv2.CascadeClassifier(R'.\resources\haarcascade_frontalface_default.xml')

# There is two ways to use this script 
# First, you can use your camera
# Second, you can use example video 
# Uncomment line with version which you want to use!

# To capture video from webcam. 
cap = cv2.VideoCapture(0)
# To use a video file as input 
# cap = cv2.VideoCapture(R'.\resources\face_video_sample.mp4')

while True:
    
    # Read the frame
    _, image = cap.read()
    
    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Detect the faces
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    # Draw the rectangle around each face
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x+w, y+h), (255, 0, 0), 2)
        
        face = image[y:y+h, x:x+w]
        cv2.imshow('Detected face', face)


        cv2.blur(image[y:y+h, x:x+w], (25, 25), image[y:y+h, x:x+w])
        

    # Display
    cv2.imshow('Video', image)

    # Stop if escape key is pressed
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

# Release the VideoCapture object
cap.release()
cv2.destroyAllWindows()
