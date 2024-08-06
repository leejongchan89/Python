coffees = dict() # empty dict

coffees['에스프레스'] = 1000
coffees['에스프레스'] = 1500 # 키값이 동일하면 value 값이 덮어쓰기된다

coffees['카페라떼'] = 2000
coffees['카푸치노'] = 3000
coffees['마키야또'] = 4000
print(coffees)

targetItem = '카페라떼'
bool = targetItem in coffees # key의 존재 유무를 확인
print(bool)

if bool:
    print('%s키가 있습니다.' % targetItem)
else:
    print('%s키가 없습니다.' % targetItem)

# Q.'핫초코'가 있는지 확인하고, 없으면 5000원으로 추가해 보세요
targetItem = '핫초코'
bool = targetItem in coffees

if not bool:
    print('%s키가 없습니다.' % targetItem)
    coffees[targetItem] = 5000
print(coffees.keys())
print(coffees.values())
print(coffees)

# Q.'6000'짜리 상품이 있는지 확인하고, 없으면 아이스커피로 추가해 보세요
price = 6000
bool = price in coffees.values()

if bool:
    print('%d원 짜리 품목이 존재합니다.' % price)
else:
    print('%d원 짜리 품목이 존재하지 않아서 추가합니다.' % price)
    coffees['아이스커피'] = price
print(coffees)

# Q. 신제품 4가지를 추가해 보세요
listCoffee = ['바닐라라떼', '라벤더', '딸기라떼', '콜드브루']

# # 확장for문 단수=key, 복수=listCoffee
# # 1
# for key in listCoffee:
#     print(key)
#
# # 2
# for idx in range(len(listCoffee)):
#     print(idx)

for idx in range(len(listCoffee)):
    coffees[listCoffee[idx]] = (idx +7) * 1000
print(coffees)

# Q. 존재하는 항목은 단가를 출력하고, 없으면 추가해 보세요
# 예외처리 try: except KeyError:
targetList = ['라벤더', '우유커피']
for key in targetList:
    try:
        price = coffees[key]
        message = '품명 : %s, 가격 : %d' % (key, price)
        print(message)
    except KeyError:
        print('%s가 존재하지 않아서 신규 추가합니다.' % key)
        coffees[key] = 5000
    # end try
# end for
print(coffees)

# ????
targetItem = '둥글레차'
price = coffees.get(targetItem, 3000)
print('품명 : %s, 가격 : %d' % (targetItem, price))
print(coffees)

# dict에서 요소 삭제
del coffees['에스프레스']
print(coffees)

# .itemS()
for (key, value) in coffees.items(): # item() = key, value 둘 다
    message = '항목 %s의 단가는 %d원입니다.' % (key, value)
    print(message)
# end for
print(coffees)

# Q. 카페라떼, 카푸치노 500원 인상  / 핫초코 500원 인하
for key in coffees.keys():
    if key == '카페라떼' or key == '카푸치노': # if key in ('카페라떼', '카푸치노'):
        coffees[key] += 500

    elif key == '핫초코':
        coffees[key] -= 500

    else:
        pass

    message = '항목 %s의 단가는 %d원입니다.' % (key, coffees[key])
    print(message)
    # end if
# end for

coffees.clear()

if len(coffees) == 0:
    print('mydixt is empty')
else:
    print('mydict is not empty')
