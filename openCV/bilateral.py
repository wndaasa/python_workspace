import sys
import numpy as np
import cv2

src = cv2.imread('.\\openCV\\lenna.bmp')

if src is None:
    print('Image load failed!')
    sys.exit()

dst = cv2.bilateralFilter(src, -1, 10, 5)

cv2.imshow('src', src)
cv2.imshow('dst', dst)

# 추가로 일반 가우시안 필터링을 만들어서 머리숲 부분을 비교해보자
cv2.waitKey()

cv2.destroyAllWindows()
