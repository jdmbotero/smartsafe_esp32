from json import FirebaseJson
from firebase_auth import FirebaseAuth
import ujson
import ufirestore
import machine
import ubinascii

def device_id():
  return str(ubinascii.hexlify(machine.unique_id()).decode('utf-8'))

def firestore_init():
  with open('localdata.json') as data_file:
    data = ujson.load(data_file)
    project_id = data["firestore"]["projectId"]
    api_key = data["firestore"]["apiKey"]
    email = data["firestore"]["email"]
    password = data["firestore"]["password"]

    auth = FirebaseAuth(api_key)
    auth.sign_in(email, password)

    ufirestore.set_project_id(project_id)
    ufirestore.set_access_token(auth.session.access_token)

def add_or_update_box(box):
  print("Updating database...")
  doc = FirebaseJson()
  doc.set("id/stringValue", device_id())
  doc.set("doorStatus/stringValue", box['doorStatus'])
  doc.set("distanceObject/doubleValue",  box['distanceObject'])
  doc.set("lightStatus/stringValue", box['lightStatus'])

  document = ufirestore.patch("boxes/" + device_id(), doc, update_mask=["id", "doorStatus", "distanceObject", "lightStatus"], bg = False)
  print("Database updated.")

def get_box_info():
  print("Getting info from database...")
  document = ufirestore.get("boxes/" + device_id())
  doc = FirebaseJson.from_raw(document)
  if doc["fields"].exists("doorAction"):
    door_action = doc["fields"].get("doorAction")
  else:
    door_action = "CLOSE"

  if doc["fields"].exists("userId"):
    connection_status = "CONNECTED"
  else:
    connection_status = "DISCONNECTED"

  print("Info obtained successfully...")
  return {"doorAction": door_action, "connectionStatus": connection_status}
  