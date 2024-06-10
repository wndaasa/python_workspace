import os
import glob
import cv2

file_list = os.listdir('.\\openCV\\images')
# img_files = [os.path.join('.\\openCV\\images', file) for file in file_list if file.endswith('.jpg')] 와 같은 코드
img_files = glob.glob('.\\openCV\\images\\*.jpg')

cv2.namedWindow('image', cv2.WINDOW_NORMAL)
cv2.setWindowProperty('image', cv2.WND_PROP_FULLSCREEN,
                      cv2.WINDOW_FULLSCREEN)

cnt = len(img_files)
idx = 0

while True:
    img = cv2.imread(img_files[idx])
    
    if img is None:
        print('Image load failed!')
        break
    
    cv2.imshow('image', img)
    if cv2.waitKey(1000) >= 0:
        break
    
    idx += 1
    if idx >= cnt:
        idx = 0
