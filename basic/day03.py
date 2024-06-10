# Q1
a = [1, 2, 3]
b = [10, 20, 30]
a.append(b)
print(a)

# Q1-1
a = [1, 2, 3]
b = [10, 20, 30]
a.extend(b)
print(a)

# Q2
nlist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(nlist)

# Q3
nlist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
nlist.insert(0, 0)
print(nlist)

# Q4
nlist.reverse()
print(nlist)

# Q5
print(f'마지막 원소 = {nlist.pop()}')
print(nlist)

# Q6
a = ['Life', 'is', 'too', 'short', 'you', 'need', 'python']
print(f'{a[4]} {a[2]}')

# Q7
s = ''
a = ['Life', 'is', 'too', 'short']
for i in range(len(a)):
    s += str(a[i]) + ' '
print(s)

# Q8
a = [1, 2, 3]
print(len(a))

# Q9
a = [1, 3, 5, 4, 2]
a.sort()
a.reverse()
print(a)

# Q10
a = [1, 2, 3, 4, 5]
a.remove(2)
a.remove(4)
print(a)

# Q11 
t = (3, )
print(t)

# Q12
t = (1, 2, 3)
t1 = (4 ,)
t = t + t1
print(t)
