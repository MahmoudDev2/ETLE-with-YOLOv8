from Utils  import LIVE, MODEL, CLASSES, annotate, recorder
from Src    import recognize_color, chooseOne, recognize_violation

from torch import empty
from torch import any as there
from ultralytics import YOLO
model = YOLO(model=MODEL)

from cv2 import VideoCapture, resize, imshow, waitKey, getWindowProperty, imwrite
no = 2
if not LIVE: cap = VideoCapture(f'./Sample/{no}.mp4')
else:
   cap = VideoCapture(0)
   cap.set(3, 1280)  # Width
   cap.set(4,  720)  # Height
   cap.set(5,   30)  # Fps

# out = recorder(f'Medium {no}', fps=30, resolution=(1280,720))

line_height = {
   'n'   : 0,
   'x'   : 0,
   'sum' : 0,
   'mean': 0
}

veh_set = empty(0)
# raw_dat = []
# data = []

# f = 2
while cap.isOpened():
   # f += 1
   # if f <= 150: continue
   success, frame = cap.read()
   if not success: break
   else:
      if frame.shape[0]>720: frame = resize(frame, None, fx=720/frame.shape[0], fy=720/frame.shape[0])

      result = model.track(frame, persist=True, classes=[n for n in CLASSES])[0].boxes.data
      traffic_lights = result[result[:,-1]==9]
      vehicles = result[result[:,-1]!=9]
      
      light_colors = recognize_color(frame, traffic_lights, print_info=False)
      chosen = chooseOne(light_colors)

      annotate(frame, traffic_lights, recognizedColor=light_colors)
      # if light_colors["yellow"]!=[]: data.append(light_colors["yellow"][0][1])
      # if light_colors["yellow"][0][1]>=73.3:
      #    imwrite(f'./Export/Before {no}TL{f}.jpg', frame)
      #    break
      if chosen[1]:
         break
         raw, pos, veh_set, violator = recognize_violation(frame, vehicles, traffic_lights[chosen[0]][:4], line_height, veh_set, imaginary_line=True)
         # raw_dat.append(raw)
         # data.append(pos)
         if there(violator): annotate(frame, violator, violationMode=True)
      # data.append(chosen[1]) if chosen[1] else data.append(0)
      # if chosen[1] == 77.08:
      #    imwrite(f'./Export/{no}TL{f}.jpg', frame)
      #    break
      # out.write(frame)
      
      # if chosen in light_colors['yellow']: imwrite(f'Export/4-{i}.jpg', frame)
      imshow('YOLOv8', frame)
      print(traffic_lights, light_colors, chosen, sep='\n')
      
      if waitKey(1) & 0xFF == 32: waitKey(0)
      if waitKey(1) & 0xFF == 27 or getWindowProperty('YOLOv8', 4) <= 0: break

cap.release()

# from numpy import array, float32, save
# raw_dat = array(raw_dat, dtype=float32)
# data = array(data)
# save(f'./Data/Raw_IL{no}.npy', raw_dat)
# save(f'./Data/Before TL{no}.npy', data)