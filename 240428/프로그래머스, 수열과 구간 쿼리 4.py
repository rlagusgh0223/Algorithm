def solution(arr, queries):
    for s, e, k in queries:
        for i in range(s, e+1):
            if i%k == 0:
                arr[i] += 1
    return arr

import sys

arr = list(map(int, sys.stdin.readline().split(", ")))
queries = list(sys.stdin.readline().strip().split("],["))
queries = [list(map(int, q.split(", "))) for q in queries]
print(solution(arr, queries))