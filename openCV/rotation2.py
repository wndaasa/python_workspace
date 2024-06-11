import cv2
import math
import numpy as np

src = cv2.imread('.\\openCV\\tekapo.bmp')
cp = (src.shape[1] / 2, src.shape[0] / 2)
rot = cv2.getRotationMatrix2D(cp, 20, 1)
dst = cv2.warpAffine(src, rot, (0, 0))

cv2.imshow('dst', dst)
cv2.waitKey()
cv2.destroyAllWindows()