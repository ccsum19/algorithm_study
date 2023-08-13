#사탕 게임

#최대 먹을 수 있는 사탕 개수 확인
def can_eat(lst):
    n = len(lst)
    answer = 1
    
    for i in range(n):
        cnt_row = 1
        cnt_col = 1
        
        for j in range(1, n):
             #먹을 수 있는 사탕 행에서 보기
            if lst[i][j] == lst[i][j - 1]:
                cnt_row += 1
                answer = max(answer, cnt_row)
            else:
                cnt_row = 1
             #먹을 수 있는 사탕 열에서 보기
            if lst[j][i] == lst[j - 1][i]:
                cnt_col += 1
                answer = max(answer, cnt_col)
            else:
                cnt_col = 1
                
    return answer
            
n = int(input())
candy = [list(input()) for _ in range(n)]
answer = 0

for i in range(n):
    for j in range(n):
        #오른쪽에 있는 사탕이랑 바꿔보기
        if j+1 < n:
            candy[i][j], candy[i][j+1] = candy[i][j+1], candy[i][j]
            temp = can_eat(candy)
            answer = max(answer, temp)
        #바꾼 사탕 원상복귀 해두기
            candy[i][j], candy[i][j+1] = candy[i][j+1], candy[i][j]
        #아래쪽에 있는 사탕이랑 바꿔보기
        if i+1 < n:
            candy[i][j], candy[i+1][j] = candy[i+1][j], candy[i][j]
            temp = can_eat(candy)
            answer = max(answer, temp)
            candy[i][j], candy[i+1][j] = candy[i+1][j], candy[i][j]

print(answer)