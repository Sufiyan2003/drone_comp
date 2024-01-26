import supervision as sv
import cv2
from ultralytics import YOLO


model = YOLO("./runs/detect/train/weights/best.pt")
image = cv2.imread("test_image.jpg")

results = model(image)[0]
detections = sv.Detections.from_ultralytics(results)
bounding_box_annotator = sv.BoundingBoxAnnotator()
label_annotator = sv.LabelAnnotator()

labels = [
    model.model.names[class_id]
    for class_id in detections.class_id
]


annotated_image = bounding_box_annotator.annotate(scene=image, detections=detections)
annotated_image = label_annotator.annotate(scene=annotated_image, detections=detections, labels=labels)
sv.plot_image(annotated_image)
