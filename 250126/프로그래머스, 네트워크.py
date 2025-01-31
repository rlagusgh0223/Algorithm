def DFS(i, computers):
    link[i] = 1
    for j in range(len(computers)):
        if computers[i][j]==1 and link[j]==0:
            link[j] = 1
            DFS(j, computers)

def solution(n, computers):
    answer = 0
    global link
    link = [0] * n
    for i in range(n):
        if link[i] == 0:
            DFS(i, computers)
            answer += 1
    return answer

import sys

n = int(sys.stdin.readline())
computers = list(sys.stdin.readline().strip().split("], ["))
computers = [list(map(int, c.split(", "))) for c in computers]
print(solution(n, computers))