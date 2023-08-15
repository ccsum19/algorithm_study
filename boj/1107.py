# 처음 생각

def check(num, broken):
    num_minus = num
    num_plus = num
    
    while num_minus in broken:
        num_minus -= 1
        
    while num_plus in broken:
        num_plus += 1
        
    if abs(num - num_minus) <= abs(num - num_plus):
        return num_minus
    else:
        return num_plus

n = input()
num = list(map(int, n))

m = int(input())
broken = set(map(int, input().split()))

if n == '100':
    print(0)
else: 
    push = []
    for i in num:
        if i in broken:
            push.append(check(i, broken))
        else:
            push.append(i)
            
    push_new = ''.join(map(str, push))  
    print(abs(int(push_new) - int(n)) + len(push_new))

# 브루트 포스

n = int(input())
m = int(input())
ans = abs(100 - n)

if m != 0: #고장난 버튼 존재
    broken = list(input().split())
else:
    broken = [] #고장난 거 없음

#이동하려고 하는 채널이 500,000까지이니까 범위는 1000000까지 갈 수 있다
for i in range(1000001):
    for j in str(i):
        # 고장난 버튼 중 하나라도 있으면
        if j in broken: 
            break
    #고장난 버튼이 없으면
    else:
        ans = min(ans, len(str(i)) + abs(i - n)) #min(숫자 버튼 수 + +- 버튼 수가 가장 적은 거 출력)

print(ans)