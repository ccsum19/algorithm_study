#소수 구하기
#에라토스테네스의 체

#입력 받기
m, n = map(int, input().split())

#소수 구하기
for i in range(m, n+1):
    #1은 소수 아님
    if i == 1:
        continue
    
    for j in range(2, int(i**0.5) + 1):
        #나누어지면 약수 존재, 소수 아님
        if i % j == 0:
            break
            
    else:
        print(i)