import cv2

src = cv2.imread('.\\openCV\\airplane.bmp', cv2.IMREAD_COLOR)
mask = cv2.imread('.\\openCV\\mask_plane.bmp', cv2.IMREAD_GRAYSCALE)
dst = cv2.imread('.\\openCV\\field.bmp', cv2.IMREAD_COLOR)

cv2.copyTo(src, mask, dst)

dst[mask > 0] = src[mask > 0]

cv2.namedWindow('src')
cv2.namedWindow('mask')
cv2.namedWindow('dst')

cv2.imshow('src', src)
cv2.imshow('mask', mask)
cv2.imshow('dst', dst)

cv2.waitKey()
cv2.destroyAllWindows()