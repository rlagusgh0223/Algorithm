def solution(arr, queries):
    for s, e in queries:
        for i in range(s, e+1):
            arr[i] += 1
    return arr

import sys

arr = list(map(int, sys.stdin.readline().split(", ")))
queries = list(sys.stdin.readline().split("],["))
queries = [list(map(int, q.split(", "))) for q in queries]
print(solution(arr, queries))