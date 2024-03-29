import cv2
from datetime import date
import datetime
import time


def record():
    cap = cv2.VideoCapture(0)
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    storage = cv2.VideoWriter(f'recordings/{datetime.datetime.now().strftime("%H-%M-%S")}.avi', fourcc, 20.0,
                              (640, 480))

    while True:
        ret, frame = cap.read()
        cv2.putText(frame, f'{datetime.datetime.now().strftime("%D-%H-%M-%S")}', (50, 50), cv2.FONT_HERSHEY_COMPLEX,
                    0.6, (255, 0, 255), 2)

        storage.write(frame)
        cv2.imshow('Press esc to Exit', frame)

        if cv2.waitKey(1) == 27:
            cap.release()
            cv2.destroyAllWindows()
            break
