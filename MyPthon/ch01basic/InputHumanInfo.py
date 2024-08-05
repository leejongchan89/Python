# end의 기본값은 enter이다. 그래서 ''값을 주면 같은 줄에 사용 가능
print('이름 입력 : ', end='')
name = input()

# input() 함수는 반환 타입이 문자열입니다.
age = int(input('나이 입력 : '))
height = float(input('키 입력 : '))

# % 포맷 코드
print('% 포맷 코드로 출력')
print('이름 : %s' % name)
print('나이 : %d' % age)
print('키 : %.2f' % height)

# .format() 문자열 함수
print('문자열 함수 format() 사용')
message = '제 이름은 {}이고, 나이는 {}세입니다.\n제 키는 {}cm입니다.'
print(message.format(name, age, height))

