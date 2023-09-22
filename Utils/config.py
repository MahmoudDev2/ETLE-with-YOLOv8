from yaml import safe_load
with open('./config.yaml', 'r') as yaml_file: CONFIG = safe_load(yaml_file)

LIVE = CONFIG['live_mode']
MODEL = './Model/yolov8x.pt' if CONFIG['model_size']=='extra large' else f"./Model/yolov8{CONFIG['model_size'][0]}.pt"
COLORS = {k: tuple(v[::-1]) for k, v in CONFIG['color_pallete'].items()}
CLASSES = CONFIG['object_classes']

PALLETES = {
   'red'    : COLORS['red'],
   'yellow' : COLORS['amber'],
   'green'  : COLORS['lime'],
   "light's off"  : COLORS['emeralad'],

   'car'       : COLORS['cyan'],
   'motorcycle': COLORS['blue'],
   'bus'       : COLORS['violet'],
   'truck'     : COLORS['fucshia'],

   'traffic light': COLORS['rose']
}