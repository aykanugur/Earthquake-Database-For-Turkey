from firebase_admin import credentials, db
import firebase_admin
import pyrebase


#THESE ARE STATIC VARIABLES
#DO NOT FORGET TO CHANGE CREDITS ,API KEY AND OTHERS

email = None
closed = False
cred = credentials.Certificate(r"***********************")
firebase_admin.initialize_app(cred, {
            'databaseURL': '***********************'
        })
fireBaseConfig = {
            "apiKey": "***********************",
            "authDomain": "***********************",
            "projectId": "***********************",
            "storageBucket": "***********************",
            "messagingSenderId": "***********************",
            "appId": "***********************",
            "measurementId": "***********************",
            "databaseURL": "***********************"
        }
firebase = pyrebase.initialize_app(fireBaseConfig)
auth_firebase = firebase.auth()
db = firebase.database()




