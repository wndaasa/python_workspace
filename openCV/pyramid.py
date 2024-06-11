import cv2

src = cv2.imread('.\\openCV\\cat.bmp')
rc = (250, 120, 200, 200)
cpy = src.copy()

cv2.rectangle(cpy, rc, (0, 0, 255), 2)
cv2.waitKey()

for i in range(1, 4):
    src = cv2.pyrDown(src)
    cpy = src.copy()
    
    cv2.rectangle(cpy, rc, (0, 0, 255), 2, shift=i)
    cv2.imshow('src', cpy)
    cv2.waitKey()
    
cv2.destroyAllWindows()
    