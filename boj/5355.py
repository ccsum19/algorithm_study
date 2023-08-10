T = int(input(""))


for k in range(T):
    R, S = input("").split()
    P = ""
    sList = list(S)
    for i in sList:
        for j in range(int(R)):
            P = P + i
    print(P)
