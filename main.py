from ultralytics import YOLO

# Load a model
model = YOLO('yolov8s.yaml')  # build a new model from YAML


# Train the model
results = model.train(data='config.yaml', epochs=15, imgsz=640)