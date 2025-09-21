import numpy as np
import cv2 as cv

img = cv.imread('images/Dogecoin.png') # image read
img = cv.resize(img, (420, 420)) # resize to 420 by 420
cv.imshow('Dogecoin', img) # image show

cv.waitKey(0) # wait for a key to be pressed
cv.destroyAllWindows() # destroy all windows

print(np.__version__)
print(cv.__version__)