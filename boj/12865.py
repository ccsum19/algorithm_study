def knapsack(k, weight, value, n):  
    V = [[0 for x in range(k+1)] for x in range(n+1)]  # DP를 위한 2차원 리스트 초기화
    for i in range(n+1):
        for w in range(k+1): 
            if i==0 or w==0:  # base
                V[i][w] = 0
            elif weight[i-1] >  w:  #용량보다 무거워서 넣을 수 없을 경우, n-1번째까지의 최적을 그대로 가져온다.
                V[i][w] = V[i-1][w]
            else: #물건의 무게가 넣을 용량 보다 작을 경우
                V[i][w] = max(value[i-1]+V[i-1][w-weight[i-1]], V[i-1][w])  # max 함수 사용하여 큰 것 선택
    return V[n][k]

n, k = map(int, input().split())
weight = [] #무게 리스트
value = [] #가치 리스트
i = 0
while i < n:
    w, v = map(int, input().split())
    weight.append(w)
    value.append(v)
    i += 1
print(knapsack(k, weight, value, n))