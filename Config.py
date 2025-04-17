#coding:utf-8

# 图片及视频检测结果保存路径
save_path = 'save_data'

# 使用的模型路径
model_path = 'runs/v8-4-pose-all2/weights/best.pt'
names = {0: 'hand-raising', 1: 'reading', 2: 'writing', 3: 'using phone',4:'bowing the head',5:'leaning over the table'}
# # class names
# names:  [ 'hand-raising', 'reading', 'writing','using phone', 'bowing the head', 'leaning over the table']
CH_names = ['举手','阅读','写作','使用手机','低头','靠在桌子上']