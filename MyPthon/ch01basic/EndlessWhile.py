# 컴퓨터가 1~100 사이의 임의의 정수 하나를 기억합니다.
# input() 함수로 숫자 1개를 입력하고, 몇 번만에 맞추는 지 체크해 보세요

import random

answer = random.randint(1, 100) # 1<= <=100
print('정답 : %d' % answer)

counter = 0 # 카운터 변수

while True:
    su = int(input('1부터 100 사이의 정수 1개 입력 : '))

    counter += 1

    if answer > su:
        print('%d보다 큰 수를 입력해 주세요.' % su)
    elif answer < su:
        print('%d보다 작은 수를 입력해 주세요.' % su)
    else:
        print('정답을 맞추셨군요')
        break
    # end if
# end While

print('%d번만에 맞추었습니다.' % counter)


