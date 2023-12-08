from collections import deque
def solution(n, edge):
    check = [0] * (n+1)
    graph = [[] for _ in range(n+1)]
    for e, d in edge:
        graph[e].append(d)
        graph[d].append(e)
    q = deque()
    q.append(1)
    check[1] = 1
    while q:
        x = q.popleft()
        for now in graph[x]:
            if check[now] == 0:
                check[now] = check[x] + 1
                q.append(now)
    answer = check.count(max(check))
    return answer


import sys
n = int(sys.stdin.readline())
edge = list(sys.stdin.readline().strip().split("], ["))
edge = [list(map(int, now.split(", "))) for now in edge]
print(solution(n, edge))