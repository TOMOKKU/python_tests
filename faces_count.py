# Import required libraries
import cv2
import numpy as np
import dlib
import random
import time
from paho.mqtt import client as mqtt_client


broker = "localhost"
port = 1883
topic = "people"
client_id = "python-mqtt-"+ str(random.randint(0, 1000))

# Connects to your computer's default camera
cap = cv2.VideoCapture(0)


# Detect the coordinates
detector = dlib.get_frontal_face_detector()

def connect_mqtt():
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(client_id)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client

def publish(client):
    # Capture frames continuously
    while True:

        # Capture frame-by-frame
        ret, frame = cap.read()
        frame = cv2.flip(frame, 1)

        # RGB to grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = detector(gray)

        # Iterator to count faces
        i = 0
        for face in faces:

            # Get the coordinates of faces
            x, y = face.left(), face.top()
            x1, y1 = face.right(), face.bottom()
            cv2.rectangle(frame, (x, y), (x1, y1), (0, 255, 0), 2)

            # Increment iterator for each face in faces
            i = i+1

            # Display the box and faces
            cv2.putText(frame, 'face num'+str(i), (x-10, y-10),cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
            print(face, i)
x
        # Display the resulting frame
        cv2.imshow('frame', frame)
        msg = int(i)
        result = client.publish(topic, msg)
        status = result[0]
        if status == 0:
            print("Send " + msg + " to topic " + topic)
        else:
            print("Failed to send message to topic " + topic)

        # This command let's us quit with the "q" button on a keyboard.
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


    # Release the capture and destroy the windows
    cap.release()
    cv2.destroyAllWindows()


def run():
    client = connect_mqtt()
    client.loop_start()
    publish(client)


if __name__ == "__main__":
    run()
