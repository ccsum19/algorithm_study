A, B = map(int, input("").split())
C = int(input(""))

IM = A*60 + B + C

M = IM%60
H = (IM/60)%24

print(int(H), int(M))




