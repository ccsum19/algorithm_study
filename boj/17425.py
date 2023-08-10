#시간 초과 난 코드
t = int(input())
for _ in range(t):
    n = int(input())
    total = 0
    for i in range(1, n+1):
        total += (n//i) * i
    print(total)
# 다른 사람 풀이를 참고하여 고친 코드
import sys
MAX = 1000000

measure = [0]*(MAX+1) #인덱스마다 약수 합 담을 배열
total = [0]*(MAX+1) #인덱스마다 약수 누적합 담을 배열

for i in range(1, (MAX+1)):
    for j in range(1, (MAX//i)+1):
        measure[i*j] += i # i의 배수에 해당하는 값들은 i를 무조건 약수로 가지고 있음. 따라서 i를 더해줌.
    total[i] = total[i-1] + measure[i] #해당 인덱스의 약수 합을 더한 누적합을 total 배열에 더함

#입력 받기    
t = int(input()) 

for _ in range(t):
    a = int(sys.stdin.readline())
    sys.stdout.write(str(total[a])+"\n")