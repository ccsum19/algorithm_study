N = int(input())


for i in range(N):
    r, e, c = map(int, input().split(" "))
    donot = r
    do = e-c
    if do == donot:
        print("does not matter")
    elif do > donot:
        print("advertise")
    elif do < donot:
        print("do not advertise")

