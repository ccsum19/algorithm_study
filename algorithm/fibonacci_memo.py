#Dynamic programming 공부
#하향식 접근, Memoization
#중복되는 부분을 없애줌

def fib_memo(n, cache):
    # base case
    if n < 3:
        return 1
        
    # 이미 n번째 피보나치를 계산했으면:
    # 저장된 값을 바로 리턴한다
    if n in cache:
        return cache[n]
    
    # 아직 n번째 피보나치 수를 계산하지 않았으면:
    # 계산을 한 후 cache에 저장
    cache[n] = fib_memo(n - 1, cache) + fib_memo(n - 2, cache)

    # 계산한 값을 리턴한다
    return cache[n]

def fib(n):
    # n번째 피보나치 수를 담는 사전
    fib_cache = {}

    return fib_memo(n, fib_cache)

# 테스트 코드
print(fib(10))
print(fib(50))
print(fib(100))

#Tabulation 방식
#상향식
def fib_tab(n):
    # 이미 계산된 피보나치 수를 담는 리스트
    fib_table = [0, 1, 1]

    # n번째 피보나치 수까지 리스트를 하나씩 채워 나간다
    for i in range(3, n + 1):
        fib_table.append(fib_table[i - 1] + fib_table[i - 2])

    # 피보나치 n번째 수를 리턴한다
    return fib_table[n]

# 테스트 코드
print(fib_tab(10))

#O(1) 최적화
def fib_optimized(n):
    current = 1
    previous = 0

    # 반복적으로 위 변수들을 업데이트한다. 
    for i in range(1, n):
        current, previous = current + previous, current

    # n번재 피보나치 수를 리턴한다. 
    return current


# 테스트 코드
print(fib_optimized(16))
print(fib_optimized(53))
print(fib_optimized(213))