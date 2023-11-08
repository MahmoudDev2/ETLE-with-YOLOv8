from torch import Tensor, tensor, cat
from cv2 import line
from numpy import ndarray

def height_TL (line_height:list, new_height:float) -> float:
   line_height['n'] += 1
   line_height['x'] = new_height
   line_height['sum'] += new_height
   line_height['mean'] = line_height['sum']/line_height['n']
   return line_height['mean']

def place_line (image:ndarray, position:float):
   position = round(position)
   line(image, (0,position), (image.shape[1],position), (0,0,0), 2)

def recognize_violation (image:ndarray, vehicles:Tensor, chosen_xyxy:Tensor, line_height:list, violator:Tensor, imaginary_line:bool=False):
   new_height = chosen_xyxy[3].item() - chosen_xyxy[1].item()
   position = 3.5 * height_TL(line_height, new_height) + chosen_xyxy[1].item()

   if imaginary_line: place_line(image, position)

   print('\n', position)
   for v in vehicles:
      veh_pos = (.5*(v[1]-v[3]) + v[3]).item()
      if veh_pos > position: violators = cat((violators, v.unsqueeze(0)), dim=0)
      print(veh_pos, end=' ')

   return violator