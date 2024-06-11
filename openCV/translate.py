import cv2
import numpy as np

# 이미지 읽기
src = cv2.imread('.\\openCV\\tekapo.bmp')

# 이동 변환 행렬 정의
trn = np.array([[1, 0, 200],
                [0, 1, 100]], dtype=np.float32)

# 이동 변환 적용
dst = cv2.warpAffine(src, trn, (0, 0))

# 결과 이미지 출력
cv2.imshow('Source Image', src)
cv2.imshow('Translated Image', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
