import cv2
import numpy as np
import os

# 작업 디렉토리를 변경합니다.
new_working_directory = os.path.abspath('openCV')
os.chdir(new_working_directory)

# 변경된 작업 디렉토리 확인
print("현재 작업 디렉토리:", os.getcwd())

# 파일 경로 설정 (변경된 작업 디렉토리 내에서 파일 경로 설정)
woman_file_path = 'woman.mp4'
raining_file_path = 'raining.mp4'

# 파일이 존재하는지 확인
if not os.path.exists(woman_file_path):
    print(f"{woman_file_path} 파일이 존재하지 않습니다. 경로를 확인하세요.")
if not os.path.exists(raining_file_path):
    print(f"{raining_file_path} 파일이 존재하지 않습니다. 경로를 확인하세요.")

# 동영상 파일 열기
cap_woman = cv2.VideoCapture(woman_file_path)
cap_raining = cv2.VideoCapture(raining_file_path)

if not cap_woman.isOpened():
    print(f"{woman_file_path} 동영상을 열 수 없습니다. 파일 경로를 확인하세요.")
if not cap_raining.isOpened():
    print(f"{raining_file_path} 동영상을 열 수 없습니다. 파일 경로를 확인하세요.")

# 두 동영상의 프레임 크기 및 FPS 맞추기
frame_width = int(cap_woman.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap_woman.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cap_woman.get(cv2.CAP_PROP_FPS)

# 결과를 저장할 비디오 작성기 초기화
out = cv2.VideoWriter('output.mp4', cv2.VideoWriter_fourcc(*'mp4v'), fps, (frame_width, frame_height))

while True:
    ret_woman, frame_woman = cap_woman.read()
    ret_raining, frame_raining = cap_raining.read()

    if not ret_woman or not ret_raining:
        print("더 이상 프레임이 없습니다. 동영상을 종료합니다.")
        break

    # woman.mp4의 프레임을 HSV 색 공간으로 변환
    hsv_frame = cv2.cvtColor(frame_woman, cv2.COLOR_BGR2HSV)
    
    # 색상 범위로 마스크 생성
    lower_bound = np.array([50, 150, 0])
    upper_bound = np.array([80, 255, 255])
    mask = cv2.inRange(hsv_frame, lower_bound, upper_bound)
    
    # 마스크의 반전
    mask_inv = cv2.bitwise_not(mask)
    
    # raining.mp4에서 동일한 크기의 프레임 추출
    frame_raining = cv2.resize(frame_raining, (frame_width, frame_height))
    
    # 크로마키 합성
    foreground = cv2.bitwise_and(frame_woman, frame_woman, mask=mask_inv)
    background = cv2.bitwise_and(frame_raining, frame_raining, mask=mask)
    combined_frame = cv2.add(foreground, background)
    
    # 결과를 저장
    out.write(combined_frame)

    # 합성된 프레임을 화면에 표시
    cv2.imshow('Combined Frame', combined_frame)
    
    # 'q' 키를 누르면 루프 종료
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 동영상 파일 닫기
cap_woman.release()
cap_raining.release()
out.release()
cv2.destroyAllWindows()
