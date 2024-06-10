import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# 물체들의 초기 위치와 속도
positions = np.array([[0, 0], [1, 0], [-1, 0]])
velocities = np.array([[0.1, 0.2], [-0.2, 0.1], [0.1, -0.1]])

# 물체들의 질량 (비슷하지만 약간의 차이가 있음)
masses = np.array([1.0, 1.1, 0.9])

# 중력 상수
G = 1

# 애니메이션을 위한 설정
fig, ax = plt.subplots(figsize=(8, 8))
ax.set_xlim([-5, 5])
ax.set_ylim([-5, 5])
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_title('3개의 물체 운동 시뮬레이션')

# 물체들을 표현할 원 객체
particles, = ax.plot([], [], 'ro', ms=10)

# 애니메이션 함수
def animate(frame):
    # 시간 증가
    dt = 0.01
    global positions
    
    # 물체들 간의 거리와 가속도 계산
    accelerations = np.zeros_like(positions)
    for i in range(len(positions)):
        for j in range(i+1, len(positions)):
            r = np.linalg.norm(positions[j] - positions[i])
            if r > 0:
                force = G * masses[i] * masses[j] / r**2
                accelerations[i] += force * (positions[j] - positions[i]) / (r * masses[i])
                accelerations[j] -= force * (positions[j] - positions[i]) / (r * masses[j])
    
    # 위치와 속도 업데이트
    velocities += accelerations * dt
    positions += velocities * dt
    
    # 애니메이션 업데이트
    particles.set_data(positions[:, 0], positions[:, 1])
    return particles,

# 애니메이션 생성 및 실행
ani = FuncAnimation(fig, animate, frames=300, interval=10, blit=True)
plt.show()