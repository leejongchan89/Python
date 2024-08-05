# coffees = [] # empty list
coffees = list()

# 리스트 안 원소 추가
coffees.append('아메리카노')
coffees.append('콜드브루')
coffees.append('카푸치노')
coffees.append('바닐라라떼')
coffees.append('디카페인커피')
coffees.append('카페라떼')

count = len(coffees)
print('요소 개수 : %d' % count)

# 인덱싱
print('앞에서 2번째 음료 : %s' % coffees[2]) # 카푸치노 가져오기
print('뒤에서 1번째 음료 : %s' % coffees[-1]) # -1은 뒤에서 1번째

# 슬라이싱 (순서가 있어야 슬라이싱 가능하다. ex) 리스트, 튜플, 문자열도 가능
print('전부 출력s' % coffees[::]) # 0~끝까지 전부다
print('1번째부터 3번째 까지 음료 : %s' % coffees[1:4])
print('3번째이후 모든 음료 : %s' % coffees[3:])
print('맨앞부터 2번째까지 음료 : %s' % coffees[:3])

# 오름차순 정렬하기 asc
coffees.sort()
print(coffees)

# 내림차순 정렬하기 desc
coffees.sort(reverse=True)
print(coffees)

import random
random.shuffle(coffees)
print(coffees)
