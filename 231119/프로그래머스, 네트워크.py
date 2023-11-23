def DFS(n, now, computers):
    global ck
    ck[now] = 1
    for i in range(n):
        if computers[now][i]==1 and ck[i]==0:
            DFS(n, i, computers)

def solution(n, computers):
    answer = 0
    global ck
    ck = [0] * n  # 방문했는지 점검
    for i in range(n):  # 이번 컴퓨터
        for j in range(n):  # 연결된 컴퓨터
            # 이번 컴퓨터와 연결된 컴퓨터가 있는데 아직 체크하지 않았다면
            if computers[i][j]==1 and ck[j]==0:
                # 그 컴퓨터와 거기에서 연결된 컴퓨터까지 체크하고 옴
                DFS(n, j, computers)
                answer += 1
    return answer


import sys
n = int(sys.stdin.readline())
computers = list(sys.stdin.readline().strip().split("], ["))
computers = [list(map(int, c.split(", "))) for c in computers]
print(solution(n, computers))