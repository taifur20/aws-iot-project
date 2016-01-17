import paho.mqtt.client as mqtt
import ssl
import json
import RPi.GPIO as GPIO
import time

# make sure python gpio library is installed
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
actionPin = 23 # Broadcom pin 23 (P1 pin 16)
GPIO.setup(actionPin, GPIO.OUT) # LED pin set as output
GPIO.output(actionPin, GPIO.LOW)

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("topic/test")

def on_message(client, userdata, msg):
    
     if str(msg.payload) == '1':
        print("Movement Detected")
        print(str(msg.payload))
        GPIO.output(actionPin, GPIO.HIGH)  # gpio pin high
        time.sleep(.1)
        GPIO.output(actionPin, GPIO.LOW)
        #time.sleep(0.075)
        
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.tls_set(ca_certs='rootCA.pem', certfile='certificate.pem.crt', keyfile='private.pem.key', tls_version=ssl.PROTOCOL_SSLv23)
client.tls_insecure_set(True)
client.connect("A3JRA11PV5KIYG.iot.us-west-2.amazonaws.com", 8883, 60)
client.loop_forever()

