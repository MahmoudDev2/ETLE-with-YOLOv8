from torch import Tensor

def place_line (traffic_light_xyxy:Tensor) -> int:
   x0,y0,x1,y1 = traffic_light_xyxy.numpy().round()
   w, h = (x1-x0, y1-y0)
   if h > w: # Vertical
      
      pass

def recognize_violation (): pass