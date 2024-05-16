"""
    # mysquare.py : 정사각형의 속성을 계산하는 모듈 
    # get_area(length):한 변의 길이가 length인 정사각형의 면적을 반환 
    # get_peri(length) : 한 변의 길이가 length인 정사각형의 둘레를 반환
    # set_pos(x, y): 좌표 (x, y)에 도형을 위치시킴
"""

xpos, ypos = 0, 0

def get_area(length): # 정사각형의 면적 계산
    """
        # 모듈 : mysquare.py 함수 : get_area(length)
        # 한 변의 길이가 length인 정사각형의 면적을 계산
    """
    return length**2

def get_peri(length): #정사각형의 둘레 계산
    """
        # 모듈 : mysquare.py 함수 : get_area(length)
        # 한변의 길이가 length인 정사각형의 면적을 계산
    """
    return 4 * length

def set_pos(x, y): # 좌표에 도형을 위치시킴
    global xpos, ypos
    xpos = x
    ypos = y
    