import cv2
import os
import numpy as np

# Setup free face detector and recognizer
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
recognizer = cv2.face.LBPHFaceRecognizer_create()

# --- USER CONFIGURATION ---
# Put your face images in a folder named 'known_faces' next to this script
# Or change the path below to your specific folder location:
path = "known_faces" 
faces, ids = [], []

# --- STEP 1: Fast Training ---
print("Training system on your photos...")
for filename in os.listdir(path):
    if filename.endswith((".jpg", ".png", ".jpeg")):
        img = cv2.imread(os.path.join(path, filename), 0)  # Load as grayscale
        detected_faces = face_cascade.detectMultiScale(img, 1.3, 5)
        for (x, y, w, h) in detected_faces:
            faces.append(img[y:y + h, x:x + w])
            ids.append(1)  # '1' represents You

recognizer.train(faces, np.array(ids))

# --- STEP 2: Live Secure Recognition ---
cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces_live = face_cascade.detectMultiScale(gray, 1.3, 5)

    status, color = "LOCKED", (0, 0, 255)

    for (x, y, w, h) in faces_live:
        roi_gray = gray[y:y + h, x:x + w]

        # PREDICT: 'id' is who it is, 'conf' is the distance (lower is better)
        id_pred, conf = recognizer.predict(roi_gray)

        # CONFIDENCE: If the distance is < 50, it's a very strong match
        if id_pred == 1 and conf < 55:
            status, color = "ACCESS GRANTED", (0, 255, 0)

        cv2.rectangle(frame, (x, y), (x + w, y + h), color, 2)
        cv2.putText(frame, f"{status} ({int(conf)})", (x, y - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 2)

    cv2.imshow('LBPH Secure Unlock', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'): break

cap.release()
cv2.destroyAllWindows()
