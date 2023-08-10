S = int(input())
N = 0
count = 0

for i in range(1, S+1):
    N += i
    count += 1
    if N > S:
        count -= 1
        break
    
print(count)
  
        
