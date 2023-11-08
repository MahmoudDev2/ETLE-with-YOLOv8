from cv2 import VideoWriter, VideoWriter_fourcc

def recorder (
   filename:str='exported',
   directory:str='./Export',
   fps:int=30,
   resolution:tuple[int]=(1280, 720)
):
   return VideoWriter(
      f'{directory}/{filename}.mp4',
      VideoWriter_fourcc(*'avc1'),
      fps,
      resolution
   )
