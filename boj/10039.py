T = int(input())
k = 2
c = 0

def gcd(A, B):
    if B == 0:
        return A
    else:
        return gcd(B, A%B)
        
for i in range(T):
    A, B = map(int, input().split(" "))
    c = gcd(A, B)
    print((A*B)//c)


            

        
    

