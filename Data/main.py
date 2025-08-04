from ultralytics import YOLO

model = YOLO("yolov8n.pt")  # También puedes usar yolov8s.pt o yolov8m.pt

# Entrenar el modelo con tus datos
results = model.train(
    data="Data\\7SG&1\\data.yaml",  # Ruta a tu archivo YAML
    epochs=50,
    imgsz=320,
    batch=16,
    name="7SD&1"
)

results
