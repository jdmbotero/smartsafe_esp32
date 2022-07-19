from json import FirebaseJson
from firebase_auth import FirebaseAuth
from uuid import uuid4
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
  print("Updating box in database...")
  doc = FirebaseJson()
  doc.set("id/stringValue", device_id())
  doc.set("doorStatus/stringValue", box['doorStatus'])
  doc.set("distanceObject/doubleValue",  box['distanceObject'])
  doc.set("lightStatus/stringValue", box['lightStatus'])

  ufirestore.patch("boxes/" + device_id(), doc, update_mask=["id", "doorStatus", "distanceObject", "lightStatus"], bg = False)
  print("Box updated.")

def get_box_info():
  print("Getting info of box from database...")
  document = ufirestore.get("boxes/" + device_id())
  doc = FirebaseJson.from_raw(document)
  if doc["fields"].exists("doorAction"):
    door_action = doc["fields"].get("doorAction")
  else:
    door_action = "CLOSE"

  if doc["fields"].exists("doorStatus"):
    door_status = doc["fields"].get("doorStatus")
  else:
    door_status = "CLOSED"

  if doc["fields"].exists("userId"):
    connection_status = "CONNECTED"
  else:
    connection_status = "DISCONNECTED"

  print("Box info obtained successfully...")
  return {"doorAction": door_action, "doorStatus": door_status, "connectionStatus": connection_status}

def add_history_box(history):
  print("Updating history in database...")
  uuid = uuid4()
  doc = FirebaseJson()
  doc.set("boxId/stringValue", device_id())
  doc.set("date/timestampValue", history['date'])
  doc.set("doorAction/stringValue", history['doorAction'])

  ufirestore.patch("history/" + str(uuid), doc, update_mask=["boxId", "date", "doorAction"], bg = False)
  print("History updated.")
  