# n만 적었을 때는 0부터 n-1
# n, m 적었을 때는 n<= <m
# 증감식 default값은 1
total = 0

for i in range(1,11,1):
    total += i
# end for (for문이 끝났다는걸 표시)

print('총합 01 : %d' % total)


# Q2. 1+4+7+…+100 = 1717
total = 0

for i in range(1,101,3):
    total += i
# end for (for문이 끝났다는걸 표시)

print('총합 02 : %d' % total)


# Q3. 97+92+87+…+7+2 = 990
total = 0

for i in range(97,1,-5):
    total += i
# end for (for문이 끝났다는걸 표시)

print('총합 03 : %d' % total)


# Q4.  1*1 + 6*6 + 11*11 + … + 96*96 = 63670
total = 0

for i in range(1,97,5):
    total += i*i
# end for (for문이 끝났다는걸 표시)

print('총합 04 : %d' % total)


# Q5.  1*2 + 2*3 + 3*4 + 4*5 + 5*6 = 70
total = 0

for i in range(1,6,1):
    total += i*(i+1)
# end for (for문이 끝났다는걸 표시)

print('총합 05 : %d' % total)

