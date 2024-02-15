def solution(arr, query):
    for i in range(len(query)):
        # 짝수 홀수를 결정하는게 query값이 아니라 query의 인덱스(순서)다
        if i%2 == 0:
            arr = arr[:query[i]+1]
        else:
            arr = arr[query[i]:]
    return arr

import sys

arr = list(map(int, sys.stdin.readline().split(", ")))
query = list(map(int, sys.stdin.readline().split(", ")))
print(solution(arr, query))