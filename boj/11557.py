T = int(input())
for i in range(T):
    N = int(input())
    name = [0]*N
    alchol = [0]*N
    Sname = ""
    num = 0
    for j in range(N):
        s, a = input().split(" ")
        name[j] = s
        alchol[j] = int(a)
        if alchol[j] > num:
            Sname = name[j]
        num = alchol[j]
    print(Sname)
