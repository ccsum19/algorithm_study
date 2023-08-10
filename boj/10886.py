N = int(input())
cute = [0]*N

for i in range(0, N):
    
    cute[i] = int(input())

if sum(cute) > N/2:
    print("Junhee is cute!")
else:
    print("Junhee is not cute!")
