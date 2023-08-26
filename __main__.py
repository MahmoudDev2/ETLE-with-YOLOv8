from Utils import MODEL, CLASSES

from ultralytics import YOLO
model = YOLO(model=MODEL)

from cv2 import VideoCapture, resize, INTER_AREA, imshow, waitKey

cap = VideoCapture('./Sample/1.mp4')
while cap.isOpened():
   success, frame = cap.read()
   if not success: break
   else:
      scale = 720/frame.shape[0]
      frame = resize(frame, None, fx=scale, fy=scale, interpolation=INTER_AREA)
      result = model.track(frame, persist=True, classes=[n for n in CLASSES])[0]
      annotated = result.plot()
      imshow('Tracking', annotated)
      if waitKey(1) & 0xFF == ord("q"): break
cap.release()
