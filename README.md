# Emotion-Based Song Recommendation (EMOTUNEHUB):

This repository contains the code for personalized music recommendations based on your emotions, delivering an immersive listening experience tailored to your mood. Discover new tracks that resonate with your emotional journey.

## Introduction
The code utilizes computer vision and deep learning techniques to recognize and classify human facial expressions. It incorporates the use of the tkinter Python library to create a user-friendly program. OpenCV, a popular computer vision library, and DeepFace, a deep learning framework, are employed to detect and classify emotions in real-time video frames. The system captures video frames, detects faces, predicts emotions, and generates an accuracy graph. Based on the detected emotion, the user is provided with song recommendations.

## Methodology
The project is structured to include several modules such as cv2, deepface, matplotlib.pyplot, sys, tkinter, and pygame. These modules serve different functionalities within the script and contribute to the seamless execution of the project.

1. Face Recognition: Video frames are captured using OpenCV and displayed to the user. When the user presses the '<space>' key, the current frame is saved and processed to detect the face region using a Haar Cascade classifier.

2. Predicted Emotion: If a face is detected, the image is cropped to include only the face region, resized, and fed into a pre-trained deep learning model to predict the emotion. The predicted emotion is displayed on the image using OpenCV's putText() function.

3. Accuracy Graph: Multiple frames are collected to generate an accuracy graph. The graph depicts the accuracy and labeled emotions. The emotion with the highest frequency and accuracy percentage is considered as the final predicted emotion.

4. Playing the Media: Pygame library is used to play an audio clip corresponding to the predicted emotion. An audio file is selected based on the predicted emotion, and the clip is played continuously until the user clicks 'stop' or 'pause'. The Pygame mixer is initialized at the beginning of the code, and the audio file is loaded and played within an if-else block.

## Classifiers
The project employs a supervised learning approach using classifiers. The Haar Cascade classifier is used to recognize faces, while the OpenCV library preprocesses images before classification. DeepFace, a deep learning framework, is used to detect and classify emotions in real-time video frames.

## Datasets
The project requires datasets for faces, emotions, and music. The main datasets used are:
- Face data: Used to identify if an image contains a face.
- Emotion data: Includes information about emotions and helps predict the emotion displayed on the face(s) in the image.
- Music data: Consists of audio files categorized based on different emotions, which are played according to the predicted emotion.

## Image Processing Techniques
Image processing techniques are employed to extract and decode faces and emotions in captured images. The main steps include image acquisition and decoding, which occur after the image has been processed.

## Applications
Emotion-Based Song Recommendation systems have various applications, including:

- Music Streaming Services: Services like Spotify, Apple Music, and Pandora can utilize emotion-based song recommendations to suggest songs to users based on their emotional state.

- Therapy and Mental Health: Music therapy often employs emotion-based approaches to improve physical, emotional, cognitive, and social functioning.

This repository serves as a demonstration of the Emotion-Based Song Recommendation system, showcasing the implementation and functionality of the code.
