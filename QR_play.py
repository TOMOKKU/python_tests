import cv2
import numpy as np
from BackgroundAudioPlay import BGAudio

cap = cv2.VideoCapture(0)
#player = cv2.VideoCapture(r'../../Videos/test.mp4')
detector = cv2.QRCodeDetector()

while True:
    ret, frame = cap.read()
    data = detector.detectAndDecode(frame)

    if data[0] != "":
        print(data[0])
        if data[0] == "test":
            bga = BGAudio("../../Videos/test.wav")
            player = cv2.VideoCapture("../../Videos/test.mp4")
            cv2.imshow("Video", np.zeros((100, 100, 3)))
            bga.play(0.0)
            while(player.isOpened()):
                ret, frame = player.read()
                if not ret:
                    break
                cv2.imshow("Video", frame)
            bga.stop()
            print("finish")


    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.releasse()
cv2.destroyAllWindows()
