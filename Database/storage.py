import pyrebase
config = {
  "apiKey": "AIzaSyAP6x6ubW2tME2Mkih5PyvOTP_K8qE0a7A ",
  "authDomain": "pwp20-c3d0d",
  "databaseURL": "https://pwp20-c3d0d.firebaseio.com",
  "storageBucket": "pwp20-c3d0d.appspot.com",
  "serviceAccount": "pwp20-c3d0d-8d0aea8fc797.json"
}


firebase = pyrebase.initialize_app(config)
storage=firebase.storage()
#storage.child("").download("")
db = firebase.database()
all_img = db.child().get()

#print(all_img.val())
for img in all_img.each():
 if img.val() != None:
  if img.val()['downloadStatus']==0:
   lat= img.val()['latitude']
   lon= img.val()['longitude']
   storage=firebase.storage()
   print(str(lat) +" "+ str(lon))
   storage.child(str(lat)+" "+str(lon)+".jpg").download("/home/dj/Work/DeepBlue/Firebase/images/"+str(lat)+" "+str(lon)+".jpg")
   db.child(img.key()).update({"downloadStatus":1})
