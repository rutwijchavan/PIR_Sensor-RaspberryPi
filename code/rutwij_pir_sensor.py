import time
from datetime import datetime
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)


led_pin=7
relay=11
PIR_Sensor=13

GPIO.setup(led_pin,GPIO.OUT)
GPIO.setup(relay,GPIO.OUT,initial=GPIO.LOW)
GPIO.setup(PIR_Sensor,GPIO.IN)


while 1:
    
    if GPIO.input(PIR_Sensor) == GPIO.HIGH:
    
      GPIO.output(relay,GPIO.HIGH)
      GPIO.output(led_pin,GPIO.HIGH)
      time.sleep(1)
      print("Motion detected")
      file = open("log.txt","a")
      file.write("Motion detected")
      file.write(datetime.today().strftime('%Y-%m-%d %H:%M:%S')+"\n")
     
    else:
         
      GPIO.output(relay,GPIO.LOW)
      GPIO.output(led_pin,GPIO.LOW)
      time.sleep(1)
      print("Motion not detected")
      file = open("log.txt","a")
      file.write("Motion not detected")
      file.write(datetime.today().strftime('%Y-%m-%d %H:%M:%S')+"\n")

file.write(datetime.today().strftime('%Y-%m-%d %H:%M:%S')+"\n")
file.close()
