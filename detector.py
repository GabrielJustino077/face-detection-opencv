import cv2

# carregar classificador de rosto
classificador = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# abrir webcam
webcam = cv2.VideoCapture(0)

while True:
    sucesso, imagem = webcam.read()

    cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

    rostos = classificador.detectMultiScale(cinza, 1.3, 5)

    for (x, y, w, h) in rostos:
        cv2.rectangle(imagem, (x,y), (x+w,y+h), (255,0,0), 2)

    cv2.imshow('Detector de Rosto', imagem)

    if cv2.waitKey(1) == 27:
        break

webcam.release()
cv2.destroyAllWindows()
