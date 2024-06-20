# DFS문제인것 같지만 전에 DFS로 풀어서 이번엔 BFS로 풀어봤다
from collections import deque


# 컴퓨터 x에 연결된 컴퓨터를 체크할 BFS
def BFS(n, computers, x):
    q = deque()
    q.append(x)
    while q:
        x = q.popleft()
        # 이번 컴퓨터 점검했다고 표시
        visit[x] = 1
        for nx in range(n):
            # 현재 컴퓨터와 연결된 다음 컴퓨터를 점검한 적이 없다면
            # q에 넣고 점검한다
            if computers[x][nx]==1 and visit[nx]==0:
                q.append(nx)


def solution(n, computers):
    answer = 0  # 네트워크의 수를 저장할 변수
    global visit  # 네트워크를 점검한 컴퓨터인지 기록할 리스트
    visit = [0] * n
    for i in range(n):
        if visit[i] == 0:
            BFS(n, computers, i)
            answer += 1
    return answer

import sys

n = int(sys.stdin.readline())
computers = list(sys.stdin.readline().strip().split("], ["))
computers = [list(map(int, c.split(", "))) for c in computers]
print(solution(n, computers))






# def DFS(n, now, computers):
#     global ck
#     ck[now] = 1
#     for i in range(n):
#         if computers[now][i]==1 and ck[i]==0:
#             DFS(n, i, computers)

# def solution(n, computers):
#     answer = 0
#     global ck
#     ck = [0] * n
#     for i in range(n):
#         for j in range(n):
#             if computers[i][j]==1 and ck[j]==0:
#                 DFS(n, j, computers)
#                 answer += 1
#     return answer