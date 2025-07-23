import cv2
import time
import csv
import os
from datetime import datetime
from ultralytics import YOLO

# Crear nombre de archivo CSV dinámico con fecha y hora actual
current_datetime = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
csv_file = f"templog_{current_datetime}.csv"

# Crear archivo CSV si no existe
with open(csv_file, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["timestamp", "temperatura"])

# Cargar modelo YOLO entrenado
model = YOLO("Data\\runs\\detect\\7SD&1\\weights\\best.pt")

# Iniciar cámara
cap = cv2.VideoCapture(0)
print("🌡️ Cámara activa para detección de temperatura. Presiona 'q' para salir.")

# Parámetros de configuración
CONFIDENCE_THRESHOLD = 0.32
MIN_HEIGHT = 40
MIN_SEPARATION = 20
last_print_time = 0
last_detected_temp = None
last_logged_minute = -1

# Clases a ignorar (por nombre o índice si fuera necesario)
IGNORED_CLASSES = [10, 11, 12]  # Por ejemplo: 10=punto, 11=guion, 12=screen (ajusta según tus etiquetas)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (3, 3), 0)
    _, thresh = cv2.threshold(blurred, 200, 255, cv2.THRESH_BINARY)
    thresh_rgb = cv2.cvtColor(thresh, cv2.COLOR_GRAY2BGR)

    results = model.predict(source=thresh_rgb, imgsz=160, conf=CONFIDENCE_THRESHOLD, verbose=False)[0]

    digits = []
    for box in results.boxes.data.tolist():
        x1, y1, x2, y2, conf, cls = box
        cls = int(cls)
        if cls in IGNORED_CLASSES:
            continue
        height = y2 - y1
        center_x = (x1 + x2) / 2

        if conf >= CONFIDENCE_THRESHOLD and height >= MIN_HEIGHT:
            digits.append((center_x, cls))

    digits.sort(key=lambda x: x[0])
    filtered_digits = []
    last_x = -float('inf')
    for d in digits:
        if abs(d[0] - last_x) > MIN_SEPARATION:
            filtered_digits.append(d)
            last_x = d[0]

    if len(filtered_digits) >= 1:
        digit_values = [d[1] for d in filtered_digits]
        try:
            temp_str = "".join(str(d) for d in digit_values)

            current_time = time.time()
            current_minute = int(current_time // 60)

            if temp_str != last_detected_temp and (current_time - last_print_time >= 1):
                print(f"🌡️ Temperatura detectada: {temp_str} °C")
                last_detected_temp = temp_str
                last_print_time = current_time

            if current_minute != last_logged_minute:
                timestamp_str = time.strftime("%Y-%m-%d %H:%M:%S")
                with open(csv_file, mode='a', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerow([timestamp_str, temp_str])
                last_logged_minute = current_minute

        except Exception:
            pass

    frame_annotated = results.plot()
    resized_frame = cv2.resize(frame_annotated, (640, 480))
    cv2.imshow("🟢 Detección de Temperatura", resized_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
