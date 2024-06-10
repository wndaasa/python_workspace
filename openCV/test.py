import cv2

# 이미지 읽기
src = cv2.imread('.\\openCV\\airplane.bmp', cv2.IMREAD_COLOR)
mask = cv2.imread('.\\openCV\\mask_plane.bmp', cv2.IMREAD_GRAYSCALE)
dst = cv2.imread('.\\openCV\\field.bmp', cv2.IMREAD_COLOR)

# copyTo 실행
cv2.copyTo(src, mask, dst)

# 결과 이미지 출력
cv2.namedWindow('dst', cv2.WINDOW_NORMAL)
cv2.imshow('dst', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
