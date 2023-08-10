# 17427 약수의 합 2

# 약수 합 구하기 (시간 초과 발생)
def sum_measure(n):
    arr = []
    for i in range(1, n+1):
        if n % i == 0:
            arr.append(i)
    return sum(arr)

n = int(input())
total = 0
for j in range(1, n+1):
    total += sum_measure(j)
print(total)

# 시간초과 X
n = int(input())

result = 0
for i in range(1, n + 1):
    result += (n // i) * i
print(result)