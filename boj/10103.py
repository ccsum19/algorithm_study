n = int(input())
C, S = (100, 100)
for i in range(n):
    c, s = map(int, input().split(" "))
    if c == s:
        C -= 0
        S -= 0
    elif c > s:
        S -= c
    else: C -= s
print(C)
print(S)
