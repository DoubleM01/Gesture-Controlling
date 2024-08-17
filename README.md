# Gesture-Controlling
## Updates
[17th Aug, 2024 --> Volume control added](volumeControl_Gesture.py)

This repository contains a simple implementation of gesture control using MediaPipe's pose estimation. The script captures video from a webcam, processes the frames to detect human pose landmarks, and visualizes the pose landmarks in real-time. 
The outout data will be used to differnt types of controlling  

## Installation
To get started with this project, you need to install the required dependencies. Make sure you have Python and pip installed on your machine.

1. Clone the repository:
```
git clone https://github.com/DoubleM01/Gesture-Controlling
cd Gesture-Controlling
```

2. Create and activate a virtual environment (optional but recommended):
```
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

3. Install the required packages:
```
pip install mediapipe opencv-python
```

## Usage & Examples
### Main Controlling "Curretly under development"
```
python gesture_controlling.py #Comming soon
```
### Volume Controlling
```
python volumeControl_Gesture.py
```
### Keypoints preview on camera 
for default camera **0**
```
python keypoints_preview.py
```
## mediapipe keypoints meaning:

### Pose keys
![mediapipe_keys](https://github.com/user-attachments/assets/d25685a9-d7e5-4fbd-96c8-0d68c80d1b5b)

### Hand keys
![mediapipe hand keys](https://mediapipe.dev/images/mobile/hand_landmarks.png)

## **Samples and Test**
**Cooming Soon**
