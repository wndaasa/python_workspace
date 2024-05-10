# Q1
money = 5000
card = False

if card == True or money >= 4000:
    print("택시를 탈 수 있습니다.")
else:
    print("택시를 탈 수 없습니다.")
    
# Q2
lucky_list = [1, 9, 23, 46]

if 23 in lucky_list:
    print("당첨")
else:
    print("꽝")
    
# Q3
num = 14

if num % 2 == 0:
    print(f'{num}은(는) 짝수입니다.')
else:
    print(f'{num}은(는) 홀수입니다.')
    
# Q4
s = '나이:30,키:180'
age = int(s[3:5])
tall = int(s[8:])

if age < 30 and tall >= 175:
    print('Yes')
else:
    print('No')
    
# Q5
sum = 0
for i in range(1, 101):
    sum += i
print(sum)

# Q6
sum = 0
for i in range(3, 1001, 3):
    sum += i
print(sum)

# Q7
A = [20, 55, 67, 82, 45, 33, 90, 87, 100, 25]
sum = 0
for i in range(len(A)):
    if A[i] >= 50:
        sum += A[i]
print(sum)

# Q8
i = 1
while(True):
    print('*' * i)
    i += 1
    if i == 5:
        break
