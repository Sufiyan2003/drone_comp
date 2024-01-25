import cv2
from ultralytics import YOLO
import numpy as np

def draw_rectangle(temp_frame, x1,y1,x2,y2):
    frame_with_rectangle = np.copy(temp_frame)
    
    if len(frame_with_rectangle.shape) == 2:
        frame_with_rectangle = cv2.cvtColor(frame_with_rectangle, cv2.COLOR_GRAY2BGR)
    color = (0,255,0)
    thickness = 2
    start_point = (x1,y1)
    end_point = (x2,y2)
    frame_with_rectangle = cv2.rectangle(frame_with_rectangle, start_point, end_point, color, thickness)
    return frame_with_rectangle    



# Load the YOLO model
model = YOLO("./runs/detect/train5/weights/best.pt")

# Open a connection to the webcam (0 is usually the default webcam)
cap = cv2.VideoCapture(0)

while True:
    # Read a frame from the webcam
    ret, frame = cap.read()

    # Perform object detection on the frame
    results = model(frame)

    for r in results:
        if len(r.boxes.xyxy) != 0:
            temp_array = r.boxes.xyxy[0].numpy()
            print(temp_array)
            frame = draw_rectangle(frame, int(temp_array[0]), int(temp_array[1]), int(temp_array[2]), int(temp_array[3]))

            
    # Display the frame with bounding boxes
    # Break the loop if the 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    cv2.imshow("frame", frame)
# Release the webcam and close all OpenCV windows
cap.release()

