import warnings
warnings.filterwarnings('ignore')
from ultralytics import YOLO

if __name__ == '__main__':
    model = YOLO('E:/00code/3.06-code/class_Detection_end/runs/v8-4-pose-all2/weights/best.pt') # 0.766 3006818 parameters, 0 gradients, 8.1 GFLOPs

    model.val(data='datasets/dataset/data.yaml',
              split='test',
              imgsz=640,
              batch=4,
              # rect=False,
              # save_json=True, # if you need to cal coco metrice
              project='runs/val',
              name='class-detect',
              iou = 0.5
              )