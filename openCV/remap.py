import cv2
import numpy as np

src = cv2.imread('.\\openCV\\tekapo.bmp')

h, w = src.shape[:2]

map2, map1 = np.indices((h, w), dtype=np.float32)
map2 = map2 + 10 * np.sin(map1 / 32)

dst = cv2.remap(src, map1, map2, cv2.INTER_CUBIC,
                borderMode=cv2.BORDER_DEFAULT)

cv2.imshow('dst', dst)
cv2.waitKey()
cv2.destroyAllWindows()     