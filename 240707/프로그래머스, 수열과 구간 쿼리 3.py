# 문제 어렵게 써놨는데
# 그냥 queries의 값을 인덱스로 받고 arr의 값을 바꾸라는거다
# ex) queries의 값 중 [0, 1]이 있다면
# arr[0]과 arr[1]의 값 바꾸기
def solution(arr, queries):
    for q in queries:
        arr[q[0]], arr[q[1]] = arr[q[1]], arr[q[0]]
    return arr

import sys

arr = list(map(int, sys.stdin.readline().split(", ")))
queries = list(sys.stdin.readline().strip().split("],["))
queries = [list(map(int, q.split(", "))) for q in queries]
print(solution(arr, queries))