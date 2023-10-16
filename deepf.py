#from keras.models import load_model
from deepface import DeepFace
import cv2
#import numpy as np
from tkinter import messagebox
import pygame
import matplotlib.pyplot as plt
from deepface import DeepFace
pygame.mixer.init()

def opencam():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        messagebox.showerror("ERROR", "Camera was not opened")

    while cap.isOpened():
        ret, frame = cap.read()
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2BGRA)
        if ret:
            cv2.imshow('CAMERA (Click Spacebar to end)', frame)
            if cv2.waitKey(25) & 0xFF == ord(' '):
                status = cv2.imwrite('capture.jpg',frame)
                if status:
                    img = cv2.imread('capture.jpg')
                    # analyze emotions using DeepFace
                    result = DeepFace.analyze(img, actions=['emotion'], enforce_detection=False)
                    
                    # extract dominant emotion and accuracy
                    emotion = result[0]['emotion']
                    dominant_emotion = max(emotion, key=emotion.get)
                    accuracy = emotion[dominant_emotion]
                    emotion = dominant_emotion
                    text = f"{emotion} ({accuracy:.2f}%)"
                    img = cv2.putText(img, text, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)
                    # display image
                    cv2.imshow('Emotion Detected', img)
                    cv2.waitKey(0)
                    cap.release()
                    cv2.destroyAllWindows()
                    return emotion
                else:
                    messagebox.showerror("ERROR","No images were written")
            emotion = None
        else:
            break
    cap.release()
    cv2.destroyAllWindows()
    return emotion
opencam()
    
def playmusic(path):
    pygame.mixer.music.load(path)
    pygame.mixer.music.play()

def stopmusic():
    pygame.mixer.music.stop()