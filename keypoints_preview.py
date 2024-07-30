#!/usr/bin/env python
# coding: utf-8

# # <center> Mediapipe Keypoints</center> #

# ## Importing Libraries ##

# ### Pose packages ###

# In[2]:


import mediapipe as mp


# ### Data packages ###

# In[5]:


import numpy as np # not used


# ### Images packages ###

# In[9]:


import cv2


# ## Initialization ##

# ### Media Pipe ###

# In[15]:


mp_pose = mp.solutions.pose
pose = mp_pose.Pose()


# ### camera ###

# In[18]:


camera_source = 0
cap = cv2.VideoCapture(camera_source)


# In[20]:


while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = pose.process(frame_rgb)
    mp.solutions.drawing_utils.draw_landmarks(frame, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)
    cv2.imshow('pose Estimation', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()


# In[ ]:




