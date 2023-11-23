from torch import Tensor, tensor, cat, isin, unique
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

def recognize_violation (image:ndarray, vehicles:Tensor, chosen_xyxy:Tensor, line_height:list, veh_set:Tensor, imaginary_line:bool=False):
   new_height = chosen_xyxy[3].item() - chosen_xyxy[1].item()
   position = 3.5 * height_TL(line_height, new_height) + chosen_xyxy[1].item()
   if imaginary_line: place_line(image, position)
   raw_position = 3.5 * new_height + chosen_xyxy[1].item()
   violators = vehicles[(vehicles[:,1]+(vehicles[:,3]-vehicles[:,1])/2)>position]
   veh_set = unique(cat((veh_set, violators[:, 4])))
   violators = vehicles[isin(vehicles[:,4], veh_set)]

   return (raw_position, position, veh_set, violators[(violators[:,1]+(violators[:,3]-violators[:,1])/2)<position])