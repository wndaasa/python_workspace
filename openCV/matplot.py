import matplotlib.pyplot as plt
import cv2

# 이미지 파일 불러오기
imgBGR = cv2.imread('.\\openCV\\cat.bmp')
# BGR파일을 RGB파일로 변환
imgRGB = cv2.cvtColor(imgBGR, cv2.COLOR_BGR2RGB)

plt.axis('off')
plt.imshow(imgRGB)
plt.show()

# 그레이스케일 이미지 출력
imgGray = cv2.imread('.\\openCV\\cat.bmp', cv2.IMREAD_GRAYSCALE)

plt.axis('off')
plt.imshow(imgGray, cmap='gray')
plt.show()
