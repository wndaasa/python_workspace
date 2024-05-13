from random import *
import numpy

word = ['location', 'love', 'month', 'earth', 'sun']
pWord = choice(word)
pStr = list()
count = 10

for i in range(len(pWord)):
    pStr.append('_')
    
print(''.join(pWord))
print()    
    
print(''.join(pStr))
print()

while(True):
    print(f'남은 도전 횟수 : {count}')    
    print()
    ch = input('단어를 한 개 입력해주세요 : ')
    for b in pWord:
        if ch in pWord:
            if ch in pStr:
                pArray = numpy.array(pStr)
            else:
                count -= 1
                print('correct!')
                print()
                pStr[pWord.index(ch)] = ch
        else:
            count -= 1
            print('worng!')
            print()
    print(''.join(pStr))
    
    if count == 0:
        print('실패하셨습니다!')
        break
    if '_' not in pStr:
        print('성공하셨습니다!')
        break