from utime import sleep
from connection import do_connect, currenttime
from firestore import firestore_init, add_or_update_box, get_box_info
from oled import oled_clean, oled_update, show_time, show_distance, show_light_status, show_door_status, show_connection_status
from ultrasonic import distance_cm
from led_rgb import rgb_on_red, rgb_on_blue
from light import light_on, light_off
from light_sensor import light_is_needed
from servomotor import open_door, close_door
from magnetic import door_is_open

do_connect()
firestore_init()
add_or_update_box({"doorStatus": "CLOSED", "distanceObject": 0.0, "lightStatus": "OFF"})

while True:
  oled_clean()
  show_time(currenttime())

  # Data from database
  box_info = get_box_info()
  if box_info["doorAction"] == "OPEN":
    open_door()
  else:
    close_door()

  if box_info["connectionStatus"] == "CONNECTED":
    rgb_on_blue()
    show_connection_status("Conectado")
  else:
    rgb_on_red()
    show_connection_status("Desconectado")

  # Data to update in database
  distance = distance_cm()
  show_distance(distance)
  if light_is_needed():
    light_status = "ON"
    light_on()
    show_light_status("Encendida")
  else:
    light_status = "OFF"
    light_off()
    show_light_status("Apagada")

  if door_is_open:
    show_door_status("Abierta")
    door_status = "OPEN"
  else:
    show_door_status("Cerrada")
    door_status = "CLOSED"

  oled_update()
  add_or_update_box({"doorStatus": door_status, "distanceObject": distance, "lightStatus": light_status})
  sleep(2)