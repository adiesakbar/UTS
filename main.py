from datetime import datetime
import csv
import cv2
from deteksi import model 
from gps_laptop import get_ip_location
from gps_module import get_gps_from_module

cap = cv2.VideoCapture(0)  # atau ganti dengan link IP Camera
 
csv_file = open('log_detection.csv', 'w', newline='')
writer = csv.writer(csv_file)
writer.writerow(['Waktu', 'Objek', 'Lat_Laptop', 'Lon_Laptop', 'Lat_Modul', 'Lon_Modul'])

while True:
    ret, frame = cap.read()
    if not ret:
        break

    result = model(frame)[0]
    deteksi = []
    for box in result.boxes:
        cls_id = int(box.cls[0])
        deteksi.append(result.names[cls_id])
    
    lat_lap, lon_lap = get_ip_location()
    lat_mod, lon_mod = get_gps_from_module()

    waktu = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    writer.writerow([waktu, ', '.join(deteksi), lat_lap, lon_lap, lat_mod, lon_mod])

    frame_plot = result.plot()
    cv2.imshow("Deteksi Objek + GPS", frame_plot)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
csv_file.close()
cv2.destroyAllWindows()
