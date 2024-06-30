# x와 연결된 송전탑의 수 계산
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
    
    # x, y가 연결된 송전탑이 끊어졌다고 가정하고
    # x를 기준으로 연결된 송전탑의 수를 구한다(cnt)
    # 전체 송전탑의 수는 n개이므로 n-cnt가 y에 연결된 송전탑의 수다
    for x, y in wires:
        global cnt
        cnt = 0
        check = [0] * (n+1)
        check[y] = 1
        DFS(x, check, graph)
        # 송전탑이 끊겼을때 두 무리의 차이가 가장 적은값을 찾는다
        answer = min(answer, abs(cnt - (n-cnt)))
    return answer

import sys

n = int(sys.stdin.readline())
wires = list(sys.stdin.readline().strip().split("],["))
wires = [list(map(int, w.split(","))) for w in wires]
print(solution(n, wires))