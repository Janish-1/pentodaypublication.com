import firebase_admin
from firebase_admin import credentials, db
from shoppinglyx.wsgi import application

# Initialize Firebase app with credentials
cred = credentials.Certificate("imp/weighty-replica-380415-firebase-adminsdk-5qps5-af7e2500f6.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://weighty-replica-380415-default-rtdb.firebaseio.com/'
})
ref = db.reference('website3')
boolean_value = ref.get()

if isinstance(boolean_value, bool) and boolean_value:
    # Perform the first action
    from shoppinglyx.wsgi import application
else:
    pass
