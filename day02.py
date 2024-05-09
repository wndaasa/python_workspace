# Q3 
rrn = '881120-1068234'
year = rrn[:2]
mon = rrn[2:4]
day = rrn[4:6]
n = rrn[7:]

print(f'{year}년 {mon}월 {day}일 생. 남은 숫자 : {n}')

# Q4
pin = '881120-1068234'
print(f'성별을 나타내는 숫자는 {pin[7]}입니다.')

# Q5
a = 'a:b:c:d'
print(a.replace(':', '#'))

# Q6
dom = 'http://naver.com'
dom = dom.replace('http://', '')
dom = dom[:dom.index('.')]
print(dom[:3] + str(len(dom)) + str(dom.count('e')) + '!')