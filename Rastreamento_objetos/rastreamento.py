# pip install opencv-python==3.4.4.19
# pip install opencv-contrib-python==3.4.4.19
import cv2
print(cv2.__version__)

rastreador = cv2.TrackerCSRT_create()

video = cv2.VideoCapture('rua.mp4')
ok, frame = video.read()

#box de interesse para ser selecionada pelo usuário
bbox = cv2.selectROI(frame)
print(bbox) #armazena pos x e y da box, e tamanho x e y

ok = rastreador.init(frame, bbox)
#print(ok)

while True:
    ok, frame = video.read()
    if not ok:
        break

    ok, bbox = rastreador.update(frame)

    if ok:
        (x, y, w, h) = [int(v) for v in bbox]
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2, 1)
    else:
        cv2.putText(frame, 'Falha rastreamento', (100, 80), cv2.FONT_HERSHEY_SIMPLEX, .75, (0, 0, 255), 2)

    cv2.imshow('Rastreando', frame)
    if cv2.waitKey(1) & 0XFF == 27:
        break
