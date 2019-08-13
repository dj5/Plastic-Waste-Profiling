'''
Script to store data generated my nn model.
Stores data in firestore according to class.
Stores location and no. of occurence
'''

import firebase_admin
import datetime
from firebase_admin import credentials
from firebase_admin import firestore
from google.cloud import storage, exceptions

# Use a service account
cred = credentials.Certificate('pwp20-c3d0d-8d0aea8fc797.json')
firebase_admin.initialize_app(cred)
db = firestore.client()

def storeafterprocess(name,lat,long):
    now = datetime.datetime.now()

    count = readcount(name,now,lat,long)
    latitude,longitude = lat,long
    doc_ref = db.collection(name).document(now.strftime("%Y-%m-%d")).collection(u'locations').document(str(lat)+" "+str(long))
    location = firestore.GeoPoint(latitude, longitude)
    doc_ref.set({
            u'location' : location,
            u'number' :count
    })


def readcount(name,date,lat,long):
    doc_ref = db.collection(name).document(date.strftime("%Y-%m-%d")).collection(u'locations').document(str(lat)+" "+str(long))
    try:
        doc = doc_ref.get()
        if doc.to_dict() == None:
            return 1

        docdict = doc.to_dict()
        count = docdict["number"]
        print(u'Document data: {}'.format(count))
        return count+1
    except exceptions.NotFound:
        print(u'No such document!')
        return 1




#storeafterprocess("pepsi",10,91)
