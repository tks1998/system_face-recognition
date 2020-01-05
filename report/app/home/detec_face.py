import face_recognition
import cv2
import time
import numpy as np

# Haarcascades
face_cascade = cv2.CascadeClassifier(
    './haarcascades/haarcascade_frontalface_alt.xml')
img = cv2.imread("data/11.png")
start = time.time()
face_rects = face_cascade.detectMultiScale(
    img, scaleFactor=1.3, minNeighbors=3)
for (x, y, w, h) in face_rects:
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 3)
end = time.time()
print("Execution time: " + str(end-start))
cv2.imshow("1", img)

# CNN dlib
# Install dlib on win: https://stackoverflow.com/questions/41912372/dlib-installation-on-windows-10
# pip install face_recognition

image = face_recognition.load_image_file("data/1.png")
start = time.time()
face_locations = face_recognition.face_locations(
    image, number_of_times_to_upsample=0, model="cnn")
for face_location in face_locations:
    top, right, bottom, left = face_location
    print("A face is located at pixel location Top: {}, Left: {}, Bottom: {}, Right: {}".format(
        top, left, bottom, right))
    x = left
    y = top
    w = right - x
    h = bottom - y

    cv2.rectangle(image, (x, y), (x+w, y+h), (0, 0, 255), 2)

end = time.time()
print("Execution time: " + str(end-start))
cv2.imshow("image", image)
cv2.waitKey(0)
