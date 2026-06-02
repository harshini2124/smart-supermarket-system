import cv2
from pyzbar.pyzbar import decode

def scan_barcode():
    cap = cv2.VideoCapture(0)
    barcode_data = None

    while True:
        _, frame = cap.read()
        for barcode in decode(frame):
            barcode_data = barcode.data.decode("utf-8")
            cap.release()
            cv2.destroyAllWindows()
            return barcode_data

        cv2.imshow("Scan Barcode", frame)
        if cv2.waitKey(1) == 27:
            break

    cap.release()
    cv2.destroyAllWindows()
