#골드바흐의 추측

import sys
num = 1000001
arr = [1 for _ in range(num)]

for i in range(2, int((num-1)**0.5)+1):
    if arr[i]:
        #자기 자신의 배수는 소수가 아니므로 0으로 변경
        for j in range(i + i, num, i):
            arr[j] = 0
            
while True:
    n = int(sys.stdin.readline())
    
    if n == 0:
        break
    
    flag = 0
    
    for k in range(3, len(arr)):
        if arr[k] and arr[n-k]:
            print(str(n) + " = " + str(k) + " + " + str(n-k))
            flag = 1
            break
    
    if flag == 0:
        print("Goldbach;s conjecture is wrong")
        
#다른 사람 풀이
import sys

prime = []
primeCheck = [0] * 1000001

for i in range(2, 1000001):
    if primeCheck[i] == 0:
        prime.append(i)
        for j in range(2*i, 1000001, i):
            primeCheck[j] = 1

while True:
    n = int(sys.stdin.readline())
    if n == 0: break
    for i in range(1, len(prime)):
        if primeCheck[n - prime[i]] == 0:
            print(f'{n} = {prime[i]} + {n - prime[i]}')
            break