import cv2
import numpy as np

# 이미지 읽기
src = cv2.imread('.\\openCV\\tekapo.bmp')

# 이동 변환 행렬 정의
aff = np.array([[1, 0.5, 0],
                [0, 1, 0]], dtype=np.float32)

h, w = src.shape[:2]

# 이동 변환 적용
dst = cv2.warpAffine(src, aff, (w + int(h * 0.5), h))

# 결과 이미지 출력
cv2.imshow('Source Image', src)
cv2.imshow('Translated Image', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
