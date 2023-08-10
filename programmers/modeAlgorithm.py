def solution(array):
    n_arr = [0] * (max(array)+1)
    answer = 0
    cnt = -1
    for i in array:
        n_arr[i] += 1
    for i in range(0, max(array)+1):
        if n_arr[i] > cnt:
            cnt = n_arr[i]
            answer = i
        elif n_arr[i] == cnt and n_arr[i] > 0:
            answer = -1
    return answer