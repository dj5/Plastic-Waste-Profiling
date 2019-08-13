import cv2
import numpy as np
import pyperclip
import os
import pandas as pd
from keras_retinanet.utils.image import read_image_bgr, preprocess_image, resize_image
ix,iy,ix2,iy2 = -1,-1,-1,-1
# mouse callback function
#global flag
import imutils
flag=0
classname="coke"
def draw_circle(event,x,y,flags,param):
    global ix,iy,ix2,iy2,flag

    if event == cv2.EVENT_LBUTTONDBLCLK:
        cv2.circle(img,(x,y),100,(255,0,0),-1)
        if flag ==0:
         ix,iy = x,y
         flag=1
        elif flag== 1:
         ix2,iy2=x,y
         flag=0
df = pd.DataFrame(columns=["Filename","x1","y1","x2","y2","classname"])
# Create a black image, a window and bind the function to window
os.chdir("/home/dj/Work/DeepBlue/FRCNN/train_data")
files =  os .listdir()
print(files)

for f in files:
 if f.find(".JPG")>-1 or f.find(".jpg")>-1 or f.find(".png")>-1 or f.find(".jpeg")>-1:
 
  img = cv2.imread(f,1)
  #img = preprocess_image(img)
  
  img=imutils.rotate(img,90)
 
  cv2.namedWindow('image',cv2.WINDOW_NORMAL)
  cv2.setMouseCallback('image',draw_circle)
 
  
  while(1):
    
    cv2.imshow('image',img)
    k = cv2.waitKey(20) & 0xFF
    if k == 27:
        break
    elif k == ord('c'):
        if flag ==0:
         abpath=os.path.abspath(f)
         iy/=6.05
         iy2/=6.05
          
         df=df.append({"Filename":abpath,"x1":ix,"y1":int(iy) ,"x2":ix2, "y2":int(iy2),"classname":classname}, ignore_index=True)
         print(df)
        #pyperclip.copy(","+str(ix)+","+str(iy))
        
        print (ix,iy,ix2,iy2)
  cv2.destroyAllWindows()
df.to_csv("data.csv", index=False)
cv2.destroyAllWindows()
