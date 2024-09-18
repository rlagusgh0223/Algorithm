def DFS(idx, check, graph):
    global cnt
    cnt += 1
    check[idx] = 1
    for i in graph[idx]:
        if check[i] == 0:
            DFS(i, check, graph)

def solution(n, wires):
    answer = n
    graph = [[] for _ in range(n+1)]
    for x, y in wires:
        graph[x].append(y)
        graph[y].append(x)
    for x, y in wires:
        global cnt
        cnt = 0
        check = [0] * (n+1)
        check[y] = 1
        DFS(x, check, graph)
        answer = min(answer, abs(cnt - (n-cnt)))
    return answer

import sys

n = int(sys.stdin.readline())
wires = list(sys.stdin.readline().strip().split("],["))
wires = [list(map(int, w.split(","))) for w in wires]
print(solution(n, wires))