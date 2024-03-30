def solution(arr, queries):
    answer = []
    # arr을 먼저 sort하고 작업하면 안되는것 같다
    # arr은 그대로 두고 그 중 s~e번째 값들을 구해서 계산하는것 같다
    for s, e, k in queries:
        # filter(조건 함수, 순회 가능한 데이터)
        tmp = list(filter(lambda x:x>k, sorted(arr[s:e+1])))
        if len(tmp) > 0:
            answer.append(tmp[0])
        else:
            answer.append(-1)
    return answer

import sys

arr = list(map(int, sys.stdin.readline().split(", ")))
queries = list(sys.stdin.readline().strip().split("],["))
queries = [list(map(int, q.split(", "))) for q in queries]
print(solution(arr, queries))