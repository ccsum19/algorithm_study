V = int(input())
who = input()
nA = 0
nB = 0

for i in range(V):
    if who[i] == 'A':
        nA += 1
    else :nB += 1

if nA == nB:
    print("Tie")
elif nA > nB:
    print("A")
else : print("B")
    
