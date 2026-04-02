import cv2

# carregar classificador de rosto
rosto_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# abrir webcam
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    cinza = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    rostos = rosto_cascade.detectMultiScale(cinza, 1.3, 5)

    for (x, y, w, h) in rostos:
        cv2.rectangle(frame, (x,y), (x+w,y+h), (255,0,0), 2)

    cv2.imshow('Detector de Rosto', frame)

    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()