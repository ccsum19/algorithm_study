a = 5*60
b = 1*60
c = 10

T = int(input())

S = 0
aN, bN, cN = (0, 0, 0)

aN = T//a
bN = (T%a)//b
cN = (T%a)%b//c
S = a*aN+b*bN+c*cN

if S != T:
    print(-1)
else:
    print(aN, bN, cN)
