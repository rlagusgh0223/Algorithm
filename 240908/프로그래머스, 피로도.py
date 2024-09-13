def DFS(k, cnt, dungeons, check):
    global answer
    answer = max(answer, cnt)
    for i in range(len(dungeons)):
        if k>=dungeons[i][0] and check[i]==0:
            check[i] = 1
            DFS(k-dungeons[i][1], cnt+1, dungeons, check)
            check[i] = 0


def solution(k, dungeons):
    global answer
    answer = 0
    check = [0] * len(dungeons)
    DFS(k, 0, dungeons, check)
    return answer

import sys

k = int(sys.stdin.readline())
dungeons = list(sys.stdin.readline().strip().split("],["))
dungeons = [list(map(int, d.split(","))) for d in dungeons]
print(solution(k, dungeons))