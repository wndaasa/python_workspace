# Q1
a = {'name' : '홍길동',
     'birth' : 1128,
     'age' : 30}
print(a)

# Q2
a = {'A' : 90,
     'B' : 80,
     'C' : 70}
print(a.pop('B'))
print(a)

# Q3
a = {'A' : 90,
     'B' : 80}
if 'C' not in a:
    print('70')
    
# Q4
a = {'A' : 90,
     'B' : 80,
     'C' : 70}
print(min(a.values()))

# Q5
a = {'A' : 90,
     'B' : 80,
     'C' : 70}
print(list(a.items()))

# Q6
fruits_dic = {'apple' : 6000,
              'melon' : 3000,
              'banana' : 5000,
              'orange' : 4000}
print(list(fruits_dic.keys()))

# Q7
print(list(fruits_dic.values()))

# Q8
print(f'fruits_dic 딕셔너리의 항목의 개수 : {len(fruits_dic)}')

# Q9
if 'apple' in fruits_dic:
    print('apple is in fruits_dic.')
if 'mango' not in fruits_dic:
    print('mango is not in fruits_dic.')
    
# Q10
a = ['a', 'b', 'c']
print(type(set(a)))

# Q11
a = [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5]
print(set(a))

# Q12
s1 = set(['a', 'b', 'c', 'd', 'e'])
s2 = set(['c', 'd', 'e', 'f', 'g'])

s1 = s1 - s2
print(s1)

# Q13
a = set()
print(type(a))

# Q14
a = {'a', 'b', 'c'}
a.update(['d', 'e', 'f'])
print(a)
