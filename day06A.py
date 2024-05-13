from functools import reduce

# Q1
def sub(a, b):
    return a - b

print(f'200 - 100 = {sub(200, 100)}')

# Q2
num = lambda x, y : x - y
print(f'200 - 100 = {num(200, 100)}')

# Q3
n_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_list = []

for i in filter(lambda x : x % 2 == 0, n_list):
    even_list.append(i)
print(even_list)

# Q4
n_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
odd_list = []

for i in filter(lambda x : x % 2 != 0, n_list):
    odd_list.append(i)
print(odd_list)

# Q5
a_list = ['a', 'b', 'c', 'd']
b_list = []
def to_upper(a):  
    for i in a:
        b_list.append(i.upper())
    return b_list
upper_a_list = to_upper(a_list)
print(upper_a_list)

# Q6
a_list = ['a', 'b', 'c', 'd']
upper_a_list = list(map(lambda x : x.upper(), a_list))
print(upper_a_list)

# Q7
n_list = [10, 20, 30]
a_list = []
b_list = []
def twice(a):
    for i in a:   
        a_list.append(i*2)
    return a_list
def triple(b):
    for i in b:   
        b_list.append(i*3)
    return b_list
print(f'입력 값의 두 배 : {twice(n_list)}')
print(f'입력 값의 세 배 : {triple(n_list)}')

# Q8
n_list = [10, 20, 30]
a_list = list(map(lambda x : x * 2, n_list))
b_list = list(map(lambda x : x * 3, n_list))
print(f'입력 값의 두 배 : {a_list}')
print(f'입력 값의 세 배 : {b_list}')

# Q9
sum_of_num = reduce(lambda x, y : x + y, range(1, 101))
print(f'1에서 100까지의 합 : {sum_of_num}')

# Q10
num = reduce(lambda x, y : x * y, range(1, 11))
print(f'10! = {num}')

# Q11
cubic = [i**3 for i in range(1,11)]
print(f'cubic = {cubic}')

# Q12
a = ['welcome', 'to', 'the', 'python', 'world']
first_a = [i[0] for i in a]
print(f'first_a = {first_a}')

# Q13
cubic = [x ** 3 for x in range(1, 11) if x ** 3 <= 500]
print('cubic = ', cubic)

# Q14
st = 'Hello 1234 Python'
str = [num for num in st if num.isdigit()]
print(str)

# Q15
class EvenCounter:
    def __init__(self, n = 0):
        self.n = n
    def __iter__(self):
        return self        
    def __next__(self):
        if self.n <= 20:
            t = self.n
            self.n += 2
            return t
        raise StopIteration
my_even = EvenCounter()
for x in my_even:
    print(x, end = ' ')
        
# Q16
fruits = 'Apple|Banana|Melon|Orange'
lst = fruits.split('|')
print(lst)