# while 구문과 양자 택일 if 구문을 사용하여 홀수와 짝수의 각각의 총합을 구해 보세요.
odd, even = 0, 0

i = 1
while i < 11:
    if i % 2 == 0:
        even += i
    else:
        odd += i
    i += 1
#end while

print('홀수의 총합 : %d' % odd)
print('짝수의 총합 : %d' % even)

