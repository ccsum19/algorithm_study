M = int(input())
N = int(input())

sqrtM = M**(1/2)
sqrtN = N**(1/2)

equal = 1

rangeM = int(sqrtM)
rangeN = int(sqrtN)

if rangeM == rangeN:
    equal = 0
if rangeM < sqrtM:
    rangeM += 1

lst = []

if rangeM!=sqrtM and equal == 0:
    print("-1")
else:
    for i in range(rangeM, rangeN+1):
        lst.append(i*i)
    print(sum(lst))
    print(min(lst))
