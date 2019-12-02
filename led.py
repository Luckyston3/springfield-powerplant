
# !/usr/bin/env python3
# -*- coding: UTF-8 -*-
import RPi.GPIO as GPIO #Importe la bibliothèque pour contrôler les GPIOs
GPIO.setmode(GPIO.BOARD) #Définit le mode de numérotation (Board)
GPIO.setwarnings(False) #On désactive les messages d’alerte
led = 37 #Définit le numéro du pin qui alimente la led
GPIO.setup(led, GPIO.OUT) #Active le contrôle du GPIO
state = GPIO.input(led) #Lit l’état actuel du GPIO, vrai si allumé, faux si éte$
if state : #Si GPIO allumé
        GPIO.output(led, GPIO.LOW) #On l’éteint
else : #Sinon
        GPIO.output(led, GPIO.HIGH) #On l’allume
