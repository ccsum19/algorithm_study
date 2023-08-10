#내 풀이
def solution(my_str, n):
    answer = []
    l = len(my_str)
    for i in range(l//n):
        answer.append(my_str[n*i:n*(1+i)])
    if l % n > 0:
        answer.append(my_str[l//n*n:])
    return answer
#다른 사람 풀이
def solution(my_str, n):
    return [my_str[i: i + n] for i in range(0, len(my_str), n)]