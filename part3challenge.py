
# coding: utf-8

# In[2]:


def videotoframe(url,frameno):
    import os
    import cv2,pafy
    import matplotlib.pyplot as plt
    #url="https://www.youtube.com/watch?v=ph7PNrAfs2A"
    videopafy=pafy.new(url)
    best=videopafy.getbest(preftype="webm")
    video=cv2.VideoCapture(best.url)
    video.set(1,frameno)
    ret,frame=video.read()
    plt.imshow(frame)
    plt.show()
    return frame

frame=videotoframe(url,frameno)
#d={'A':[frame.flatten()],'B':[1]}
v=frame.flatten()
vdct=dct(v)[:30]

A=','+','.join(map(str,vdct.tolist()))

#test variable
model.predict(A)

