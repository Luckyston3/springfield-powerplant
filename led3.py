# !/usr/bin/env python3
# -*- coding: UTF-8 -*-
import RPi.GPIO as GPIO #Importe la bibliothèque pour contrôler les GPIOs
import time
GPIO.setmode(GPIO.BOARD) #Définit le mode de numérotation (Board)
GPIO.setwarnings(False) #On désactive les messages d’alerte
led = 37 #Définit le numéro du pin qui alimente la led
GPIO.setup(led, GPIO.OUT) #Active le contrôle du GPIO
state = GPIO.input(led) #Lit l’état actuel du GPIO, vrai si allumé, faux si éteint
for i in range(1,11):	
	GPIO.output(led, GPIO.HIGH) #On l’éteint
	time.sleep(0.5)
	GPIO.output(led, GPIO.LOW)
	time.sleep(0.5)
