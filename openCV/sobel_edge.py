import cv2
import numpy as np

src = cv2.imread('.\\openCV\\lenna.bmp', cv2.IMREAD_GRAYSCALE)

dx = cv2.Sobel(src, cv2.CV_32F, 1, 0)
dy = cv2.Sobel(src, cv2.CV_32F, 0, 1)

mag = cv2.magnitude(dx, dy)
mag = np.clip(mag, 0, 255).astype(np.uint8)

dst = np.zeros(src.shape[:2], np.uint8)
dst[mag > 120] = 255

cv2.imshow('mag', mag)
cv2.imshow('dst', dst)

cv2.waitKey()
cv2.destroyAllWindows()