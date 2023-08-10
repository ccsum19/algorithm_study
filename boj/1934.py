N = int(input())
S = 0

for i in range(N):
    a, b, c = map(int, input().split(" "))
    
    if a == b == c:
        S = max(S, 10000+a*1000)
    elif a == b or a == c:
        S = max(S, 1000+a*100)
    elif b == c:
        S = max(S, 1000+b*100)
    else:
        S = max(S, 100 * max(a, b, c))

print(S)

    
        
        



