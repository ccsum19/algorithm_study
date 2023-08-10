#알고리즘 수업 - 퀵 정렬 1
# 이 문제는 파이썬으로 풀 수 없다. (메모리 초과, 시간초과)
#결국 제출은 pypy3로 하였다. 

import sys
sys.setrecursionlimit(int(1e4))
input = sys.stdin.readline

#리스트의 인덱스를 교환하는 함수
def switch(lst, i, j):
    change.append([lst[i], lst[j]])
    temp = lst[i]
    lst[i] = lst[j]
    lst[j] = temp
    return

#나눠서 교환하는 partition 함수 작성
def partition(lst, p, r):
    x = lst[r]
    i = p - 1
    for j in range(p, r):
        if lst[j] <= x:
            i += 1
            switch(lst, i, j)
    if i + 1 != r:
        switch(lst, i+1, r)
    return i + 1
    
#quick_sort 함수 작성 (오름차순 정렬)
def quick_sort(lst, p = 0, r = None):
    if r == None:
        r = len(lst) - 1
    if r - p < 1:
        return
    else:
        pivot = partition(lst, p, r)
        quick_sort(lst, p, pivot - 1)
        quick_sort(lst, pivot + 1, r)
#입력
n, k = map(int, input().strip().split()) #n은 배열의 크기
arr = list(map(int, input().strip().split()))
change = []
quick_sort(arr)
if len(change) < k:
    print(-1)
else:
    print(change[k-1][1], change[k-1][0])
    
    
    