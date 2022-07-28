import cv2
import os

cap = cv2.VideoCapture(0)

w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = int(cap.get(cv2.CAP_PROP_FPS))
print("image wid: ", w)
print("image height: ", h)
print("frame rate: ", fps)

resize = 1

cascade_dir = './opencv-master/data/haarcascades'
cascade_xml = 'haarcascade_frontalface_default.xml'
cascade = os.path.join(cascade_dir, cascade_xml)
faceCascade = cv2.CascadeClassifier(cascade)
cap.set(cv2.CAP_PROP_FPS, 5)
fps = int(cap.get(cv2.CAP_PROP_FPS))
print("frame rate: ", fps)

while(cap.isOpened()):
     ret, frame = cap.read()
     frame_resized = cv2.resize(frame, (int(int(w)/resize), int(int(h)/resize)))
     frame_gray = cv2.cvtColor(frame_resized, cv2.COLOR_BGR2GRAY)
     faces = faceCascade.detectMultiScale(frame_gray, scaleFactor=1.2, minNeighbors=2, minSize=(2, 2))
     i = 0
     for fx, fy, fw, fh in faces:
         cv2.rectangle(frame_resized, (fx, fy), (fx+fw, fy+fh), (255, 0, 0), 2)
     cv2.imshow('webcam', frame_resized)
     i = i+1
     print(i)
     key = chr(cv2.waitKey(1) & 0xff)
     if key == 'q':
         break
     elif key == 's':
         cv2.imwrite('cap_raw.png', frame)
         cv2.imwrite('cap_resized.png', frame_resized)
         cv2.imwrite('cap_gray.png', frame_gray)
         print("Saved image")
     else:
         pass

cap.release()
cv2.destroyAllWindows()
