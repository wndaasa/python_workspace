import cv2
import numpy as np

def cartoon_filter(img):
    h, w = img.shape[:2]
    img2 = cv2.resize(img, (w // 2, h // 2))

    blr = cv2.bilateralFilter(img2, -1, 20, 7)
    edge = 255 - cv2.Canny(img2, 80, 120)
    edge = cv2.cvtColor(edge, cv2.COLOR_GRAY2BGR)

    dst = cv2.bitwise_and(blr, edge)
    dst = cv2.resize(dst, (w, h), interpolation=cv2.INTER_NEAREST)

    return dst

def pencil_sketch(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blr = cv2.GaussianBlur(gray, (0, 0), 3)
    dst = cv2.divide(gray, blr, scale=255)
    return cv2.cvtColor(dst, cv2.COLOR_GRAY2BGR)

cap = cv2.VideoCapture(0)  # 카메라에서 입력 받기
mode = 0  # 필터 모드: 0 - 원본, 1 - 카툰, 2 - 스케치

while True:
    ret, frame = cap.read()
    if not ret:
        break

    if mode == 1:
        frame = cartoon_filter(frame)
    elif mode == 2:
        frame = pencil_sketch(frame)

    cv2.imshow('frame', frame)
    
    key = cv2.waitKey(1)
    
    if key == 27:  # 'Esc' 키를 누르면 종료
        break
    elif key == 32:  # 'Space' 키를 누르면 모드 변경
        mode = (mode + 1) % 3

cap.release()
cv2.destroyAllWindows()
