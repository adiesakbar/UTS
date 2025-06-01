# deteksi.py
from ultralytics import YOLO
import cv2
import serial  # untuk komunikasi ke Arduino
import time

# === INISIALISASI SERIAL ===
arduino = serial.Serial('COM3', 9600)  # Ganti dengan port Arduino kamu
time.sleep(2)  # Tunggu Arduino siap

# === INISIALISASI YOLO ===
model = YOLO('yolov8n.pt')
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    result = model(frame)[0]
    annotated_frame = result.plot()

    # Cek apakah deteksi objek tertentu muncul
    for box in result.boxes:
        class_id = int(box.cls[0])
        class_name = model.names[class_id]

        print("Terdeteksi:", class_name)

        if class_name == 'person':  # Misal: kirim '1' kalau deteksi manusia
            arduino.write(b'1')
        else:
            arduino.write(b'0')

    cv2.imshow("YOLOv8 Detection", annotated_frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
arduino.close()

