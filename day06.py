# Q1
def is_odd(num):
    if num % 2 == 0:
        print(f'{num}은(는) 짝수입니다.')
    else:
        print(f'{num}은(는) 홀수입니다.')
is_odd(2)

# Q2
def nAvg(*args):
    num_sum = sum(args) 
    num_avg = num_sum / len(args)
    print(f'평균값은 {num_avg}입니다.')    
nAvg(2, 3, 5, 3, 2)

# Q3
def gugudan(n):
    if n <= 1 or n >= 10:
        print('2부터 9까지의 자연수를 입력하세요')
        return
    else:
        for i in range(1, 10):
            print(f'{n} x {i} = {n * i}')
gugudan(3)
        
    