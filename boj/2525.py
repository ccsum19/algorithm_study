A, B, C= map(int, input("").split())
D = int(input(""))

IM = A*60*60 + B*60 + C + D

S = IM%60
M = (IM/60)%60
H = (IM/(60*60))%24

print(IM, int(H), int(M), int(S))




