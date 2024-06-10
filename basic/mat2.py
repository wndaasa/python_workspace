import matplotlib.pyplot as plt
import numpy as np

grid = plt.GridSpec(3, 3, wspace=0.4, hspace=0.3)

# 정규 분포 그리기 --> 0행 0열 ~ 0행 2열까지
X = np.random.randn(100)
Y = np.random.randn(100)
plt.subplot(311).scatter(X, Y)

# 점선 그리기
plt.subplot(grid[1, :2]).plot([1, 2, 3, 4, 5], linestyle="--", color='red')

# cos 함수 그리기
X = np.linspace(0, 10, 100)
Y = np.cos(X)
plt.subplot(337).plot(X, Y, color='green')

# 막대 차트 그리기
X = np.arange(10)
Y = np.random.uniform(1, 10, 10)
plt.subplot(338).bar(X, Y)

# 2D 이미지 그리기
Z = np.random.uniform(0, 10, (8, 8))
plt.subplot(grid[1:, 2]).imshow(Z, aspect='auto')

plt.show()
