import matplotlib.pyplot as plt
from matplotlib import gridspec
import numpy as np

# 산점도 데이터
x_scatter = np.random.rand(100)
y_scatter = np.random.rand(100)

# 막대 그래프 데이터
x_bar = np.arange(10)
y_bar = np.random.randint(1, 101, 10)

# 이미지 데이터
img = np.random.rand(100, 100, 3)

# 그래프 객체 생성
fig = plt.figure(figsize=(10, 6))
gs = gridspec.GridSpec(1, 3, width_ratios=[2, 1, 1])

# 산점도 그리기
ax1 = plt.subplot(gs[0])
ax1.scatter(x_scatter, y_scatter)

# 막대 그래프 그리기
ax2 = plt.subplot(gs[1])
ax2.bar(x_bar, y_bar)

# 이미지 표시
ax3 = plt.subplot(gs[2])
ax3.imshow(img)

# 레이블 및 제목 추가
ax1.set_title("산점도")
ax2.set_title("막대 그래프")
ax3.set_title("이미지")

# 축 설정
ax1.set_xlabel("X 축")
ax1.set_ylabel("Y 축")
ax2.set_xlabel("X 축")
ax2.set_ylabel("Y 축")

# 그래프 레이아웃 조정
plt.tight_layout()

# 그래프 표시
plt.show()