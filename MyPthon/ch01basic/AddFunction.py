def add(first, second): # first = 10 이라고 적으면 default값을 주는거다.
    return first + second

su01 = 14
su02 = 5

result = add(su01, su02) # positional argument
print('%d + %d = %d' % (su01, su02, result))

result = add(first=10, second=20) # keyword argument
print('%d + %d = %d' % (10, 20, result))

result = add(100, 200)
print('%d + %d = %d' % (su01, su02, result))