import os
os.chdir("/home/dj/Work/DeepBlue/keras-frcnn-master/train_data/pepsi_train")
files =  os .listdir()
counter=1
for f in files:
 if f.find("png")>-1:
        os.rename(f, str(counter)+".png")
 elif f.find("jpg")>-1:
        os.rename(f, str(counter)+".jpg")
 elif f.find("jpeg")>-1:
        os.rename(f, str(counter)+".jpeg")
 counter=counter+1
