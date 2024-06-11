import cv2
import numpy as np

# 이미지 읽기
logo = cv2.imread('.\\openCV\\opencv-logo-white.png', cv2.IMREAD_UNCHANGED)  # 알파 채널 포함
dst = cv2.imread('.\\openCV\\cat.bmp', cv2.IMREAD_COLOR)

# 로고 이미지가 잘 읽혔는지 확인
if logo is None or dst is None:
    print("이미지 읽기 실패")
    exit()

# 로고 이미지의 크기 가져오기
logo_h, logo_w = logo.shape[:2]

# 로고의 RGBA 채널 분리
b, g, r, a = cv2.split(logo)

# 알파 채널을 마스크로 사용
mask = a

# 배경 제거된 로고 만들기
logo_bgr = cv2.merge((b, g, r))

# 고양이 이미지에 로고를 합성할 위치 설정 (좌측 상단)
top_left = (0, 0)
bottom_right = (top_left[0] + logo_w, top_left[1] + logo_h)

# 관심 영역(ROI) 설정
roi = dst[top_left[1]:bottom_right[1], top_left[0]:bottom_right[0]]

# ROI에 로고를 합성
roi[mask > 0] = logo_bgr[mask > 0]

# 합성된 결과를 원본 이미지에 적용
dst[top_left[1]:bottom_right[1], top_left[0]:bottom_right[0]] = roi

# 결과 이미지 출력
cv2.namedWindow('dst', cv2.WINDOW_NORMAL)
cv2.imshow('dst', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
