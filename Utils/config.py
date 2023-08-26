from yaml import safe_load
with open('./config.yaml', 'r') as yaml_file: CONFIG = safe_load(yaml_file)

MODE = CONFIG['input_mode'][0]

size = CONFIG['model_size'][0]
MODEL = './Model/yolov8x.pt' if size=='extra large' else f'./Model/yolov8{size[0]}.pt'

CLASSES = CONFIG['object_classes']
