x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())

p1 = [x1, y1]
p2 = [x2, y2]
p3 = [x3, y3]
p4 = [x4, y4]

# 안 만나는 경우 제외 
if min(x1, x2) > max(x3, x4) or min(x3, x4) > max(x1, x2) or \
    min(y1, y2) > max(y3, y4) or min(y3, y4) > max(y1, y2):
    print(0)
    quit()
    
# 벡터를 연산 하는 함수 
def ccw(p1, p2, p3):
    v1 = [p2[0] - p1[0], p2[1] - p1[1]]
    v2 = [p3[0] - p2[0], p3[1] - p2[1]]
    return v1[0] * v2[1] - v1[1] * v2[0] # 벡터 외적

def calc():
    a1 = p2[1] - p1[1]
    b1 = p1[0] - p2[0]
    c1 = p1[0] * p2[1] - p2[0] * p1[1]
    
    a2 = p4[1] - p3[1]
    b2 = p3[0] - p4[0]
    c2 = p3[0] * p4[1] - p4[0] * p3[1]
    
    x = (b2 * c1 - b1 * c2) / (a1 * b2 - a2 * b1)
    y = (a2 * c1 - a1 * c2) / (a2 * b1 - a1 * b2)
    
    return [x, y]

a = ccw(p1, p2, p3) * ccw(p1, p2, p4)
b = ccw(p3, p4, p1) * ccw(p3, p4, p2)

if a <= 0 and b <= 0:
    print(1)
    
    if (x4 - x3) * (y2 - y1) == (x2 - x1) * (y4 - y3):
        if max(x1, x2) == min(x3, x4) or max(x3, x4) == min(x1, x2):
            if p1 in [p3, p4]: print(*p1)
            elif p2 in [p3, p4]: print(*p2)
        else: print(*calc())
    else: print(0)