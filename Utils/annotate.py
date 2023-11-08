from numpy import ndarray
from torch import Tensor

def current_color (n:int, recognizedColor) -> str:
   for key, values in recognizedColor.items():
      for data in values:
         if data[0]==n: return key

def annotate (frame:ndarray, prediction:Tensor, recognizedColor={}, violationMode:bool=False, scale:float=.5, padding:int=6):

   from cv2 import rectangle, getTextSize, putText
   from torch import ceil, floor
   from Utils import CLASSES, PALLETES

   for n,row in enumerate(prediction):
      if violationMode:
         label = f'{row[5]*100:.2f}% {CLASSES[int(row[6])].title()} VIOLATES'
         pass
      else: label = f'{row[4].to(int)}. {row[5]*100:.2f}% {CLASSES[int(row[6])].title()}' if not recognizedColor else f'{row[5]*100:.2f}% {current_color(n, recognizedColor).upper()}'
      color = PALLETES[CLASSES[int(row[6])]] if not recognizedColor else PALLETES[current_color(n, recognizedColor)]

      x1 = int(ceil(row[0]))
      y1 = int(ceil(row[1]))
      x2 = int(floor(row[2]))
      y2 = int(floor(row[3]))
      rectangle(frame, (x1,y1), (x2,y2), color, padding//2)

      w_label, h_label = getTextSize(label, 0, scale, int(scale*2))[0]
      rectangle(frame, (x1, y1-h_label-2*padding), (x1+w_label+2*padding, y1), color, -1)
      
      putText(frame, label, (x1+padding, y1-padding), 0, scale, (0,0,0), int(scale*2), 16)
