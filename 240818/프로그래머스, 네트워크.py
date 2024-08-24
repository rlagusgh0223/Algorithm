def DFS(x, computers):
    visit[x] = 1
    for nx in range(len(computers[x])):
        if computers[x][nx]==1 and visit[nx]==0:
            DFS(nx, computers)

def solution(n, computers):
    answer = 0
    global visit
    visit = [0] * n
    for i in range(n):
        if visit[i] == 0:
            DFS(i, computers)
            answer += 1
    return answer

import sys

n = int(sys.stdin.readline())
computers = list(sys.stdin.readline().strip().split("], ["))
computers = [list(map(int, c.split(", "))) for c in computers]
print(solution(n, computers))