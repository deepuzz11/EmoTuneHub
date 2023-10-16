from deepface import DeepFace
import cv2
from tkinter import messagebox
import pygame
import matplotlib.pyplot as plt
from deepface import DeepFace

pygame.mixer.init()

def openc():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        messagebox.showerror("ERROR", "Camera was not opened")
    accuracies = []
    emo=[]
    num_images = 0
    while cap.isOpened() and num_images < 5: # capture 5 images
        ret, frame = cap.read()
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2BGRA)
        if ret:
            cv2.imshow('CAMERA (Click Spacebar to end)', frame)
            if cv2.waitKey(25) & 0xFF == ord(' '):
                status = cv2.imwrite('capture.jpg',frame)
                if status:
                    face_cascade = cv2.CascadeClassifier('C:\\Users\\deepi\\PYTHON PROJECT\\haarcascade_frontalface_default.xml')
                    img = cv2.imread('C:\\Users\\deepi\\PYTHON PROJECT\\capture.jpg')
                    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5,minSize=(30, 30)) 
                    if len(faces)>0:
                        result = DeepFace.analyze(img, actions=['emotion'], enforce_detection=False)
                        
                        # extract dominant emotion and accuracy
                        emotion = result[0]['emotion']
                        dominant_emotion = max(emotion, key=emotion.get)
                        accuracy = emotion[dominant_emotion]
                        emotion = dominant_emotion
                        text = f"{emotion} ({accuracy:.2f}%)"
                        emo.append(emotion)
                        img = cv2.putText(img, text, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)
                        accuracies.append(accuracy)
                        num_images += 1
                        # display image
                        cv2.imshow('Emotion Detected', img)
                        cv2.waitKey(0)
                    else:
                        messagebox.showerror("ERROR", "No faces were detected")
                else:
                    messagebox.showerror("ERROR","No images were written")
            emotion = None
        else:
            break
    cap.release()
    cv2.destroyAllWindows()
    plt.plot(accuracies)
    plt.title("Accuracy of Dominant Emotion Over Time")
    plt.xlabel("Image Captured")
    plt.ylabel("Accuracy")
    plt.show()
    g=emo[0]
    for i in range(len(accuracies)-1):
        if accuracies[i+1]>accuracies[i]:
            g=emo[i]
    return g
        
        
    


def playmusic(path):
    pygame.mixer.music.load(path)
    pygame.mixer.music.play()

def stopmusic():
    pygame.mixer.music.stop()