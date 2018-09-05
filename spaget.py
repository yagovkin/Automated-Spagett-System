import numpy as np
import pygame
import cv2
import datetime as dt

lastTime = dt.datetime.now()
currentTime = dt.datetime.now()

pygame.mixer.init()

pygame.mixer.set_num_channels(8)

voice = pygame.mixer.Channel(2)

spagetSound = pygame.mixer.Sound("spaghett-1.wav")

cap = cv2.VideoCapture(0)

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

while(True):
    frame = cap.read()[1]

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    if len(faces) > 0:
        if voice.get_busy() == False:
            if (currentTime - lastTime).seconds > 3:
                lastTime = dt.datetime.now()
                voice.play(spagetSound)
                print("SPAGET!")

    for (x,y,w,h) in faces:
        cv2.rectangle(gray, (x,y), (x+w, y+h), (255,0,0),2)

        currentTime = dt.datetime.now()

    cv2.imshow('frame',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break