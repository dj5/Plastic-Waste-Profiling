import keras
from keras_retinanet import models
from map import map
from chart2 import chart
# for visualization only
from keras_retinanet.utils.image import read_image_bgr, preprocess_image, resize_image
#from keras_retinanet.utils.visualization import draw_box, draw_caption
#from keras_retinanet.utils.colors import label_color
#import matplotlib.pyplot as plt

import cv2
import os
import shutil
import numpy as np
import time

import mtd # firestore upload
from storage import storage
import tensorflow as tf
import pandas as pd
df=pd.DataFrame(columns=["Name","class"])
df2=pd.DataFrame(columns=["Name","class"])
df3=pd.DataFrame(columns=["Name","class"])
storage()
def get_session():
    config = tf.ConfigProto()
    config.gpu_options.allow_growth = True
    return tf.Session(config=config)
keras.backend.tensorflow_backend.set_session(get_session())
model_path = 'snapshots/resnet152_csv_110.h5'

# load retinanet model
model = models.load_model(model_path, backbone_name='resnet152')

model = models.convert_model(model)




print(model.summary())
img_path = "/home/dj/Work/DeepBlue/Firebase/images"
# load label to names mapping for visualization purposes
labels_to_names ={0: 'maggi', 1: 'pepsi',2:'cadbury'}
print(os.listdir(img_path))
for idx,img_name in enumerate(sorted(os.listdir(img_path))):
 if not img_name.lower().endswith(('.bmp', '.jpeg', '.jpg', '.png', '.tif', '.tiff')):
  continue
 latlon = img_name.split(' ')
 #print(latlon)
 latlon[1]=latlon[1][:-4]
 print(img_name)
 image = cv2.imread(img_path+'/'+img_name)
 #image=cv2.resize(image, (640, 640))
#storeafterprocess("pepsi",10,91)




#preprocess image for network
 image = preprocess_image(image)
 image, scale = resize_image(image)

# process image
 start = time.time()

 boxes, scores, labels =model.predict_on_batch(np.expand_dims(image, axis=0))
 print("processing time: ", time.time() - start)

# correct for image scale
 boxes /= scale

# visualize detections
 for box, score, label in zip(boxes[0], scores[0], labels[0]):
    if label < 0:
        break
    print(labels_to_names[label])

    df=df.append({"Name":img_name,"class":labels_to_names[label]},ignore_index=True)
    df.to_csv(labels_to_names[label]+'.csv',mode='a', header=False)
  
    if score < 0.5: # score less than 50% break
        break
    
    
        
    mtd.storeafterprocess(labels_to_names[label],float(latlon[0]),float(latlon[1]))
 shutil.move(img_path+'/'+img_name,"/home/dj/Work/DeepBlue/Firebase/old_images/"+img_name)
 map()
 chart()

