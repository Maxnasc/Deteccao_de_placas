import cv2
webcam = cv2.VideoCapture(0)
classificadorVideoFace = cv2.CascadeClassifier('stop_data.xml')

if webcam.isOpened():
    validacao, frame = webcam.read()
    cv2.waitKey()
    
    while validacao:
        validacao, frame = webcam.read()
        
        cinza = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        detecta = classificadorVideoFace.detectMultiScale(cinza, scaleFactor=1.5, minSize=(150, 150))
        #detecta = classificadorVideoFace.detectMultiScale(cinza)
        
        for(x, y, l, a) in detecta:
            cv2.rectangle(frame, (x, y), (x + l, y + a), (0, 255, 0), 2)
        
        cv2.imshow('camera', frame)
        key = cv2.waitKey(2) 
        if key == 27: #ESC
            break
    
    cv2.imwrite('foto camera.png', frame)
    
webcam.release()
cv2.destroyAllWindows()