#coding: utf-8
import Adafruit_DHT
import RPi.GPIO as GPIO
import time
sensor = Adafruit_DHT.DHT11
pin = 26
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
led = 40
GPIO.setup(led, GPIO.OUT)
#Active le contrôle du GPIO
while True:#boucle infinie, il faudra interompre le programme avec Ctrl + C
  humidite, temperature = Adafruit_DHT.read_retry(sensor, pin)
  if humidite > 50:
    GPIO.output(led, GPIO.HIGH) #On allume la led
    print("alerte! l’humidité est "+str(humidite)+"%")
  else:
    GPIO.output(led, GPIO.LOW) #On éteint la led
    print("tout va bien, l’humidité est "+str(humidite)+"%")
    time.sleep(0.2)
