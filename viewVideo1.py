import numpy as np
import cv2 as cv

video = cv.VideoCapture('videos/ElonSalute.mp4') # video capture

if video.isOpened() == False: # check if video is opened
    print("Error: Could not open video")

while True: # while video is opened
    check, frame = video.read() # read frame
    if check == True:
        cv.imshow('Frame', frame) # show frame

        if cv.waitKey(25) & 0xFF == 27: # wait for escape key to be pressed
            break
    else:
        break

video.release() # release video
cv.destroyAllWindows() # destroy all windows

print(np.__version__)
print(cv.__version__)