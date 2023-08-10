# 약수
n = int(input()) # 약수 개수
arr = list(map(int, input().split())) # 약수
N = min(arr) * max(arr)
print(N)