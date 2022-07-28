import cv2
import webbrowser

cap = cv2.VideoCapture(0)

detector = cv2.QRCodeDetector()

while True:
    ret, frame = cap.read()
    data = detector.detectAndDecode(frame)

    if data[0] != "":
        print(data[0])
        idata = str(data[0])
        webbrowser.open(idata, new=0, autoraise=True)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.releasse()
cv2.destroyAllWindows()
