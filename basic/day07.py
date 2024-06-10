# Q1
input1 = eval(input('첫번째 숫자를 입력하세요 : '))
input2 = eval(input('두번째 숫자를 입력하세요 : '))

total = input1 + input2
print('두 수의 합은 %s입니다.' % total)

# Q2
nList = list(input().split(','))
nList = map(int, nList)
print(sum(nList))

