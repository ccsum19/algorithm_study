#2와 5로 나누어 떨어지지 않는 정수 n(1 ≤ n ≤ 10000)가 주어졌을 때, 각 자릿수가 모두 1로만 이루어진 n의 배수를 찾는 프로그램을 작성하시오.

def check(n):
    one = 1
    cnt = 1
    while True:
        #1로 이루어진 수가 배수가 아닌 경우
        if one % n != 0:
            #다음 1로만 이루어진 수로 바꿈
            one = one * 10 + 1
            cnt += 1 #자리수 증가   
        else:
            #배수 찾음
            return cnt
    
while True:
    try:
        n = int(input())
        print(check(n))
    except:
        break