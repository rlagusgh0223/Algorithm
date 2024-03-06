def DFS(n, check, graph):
    global cnt
    cnt += 1
    check[n] = 1
    for now in graph[n]:
        if check[now] == 0:
            DFS(now, check, graph)

def solution(n, wires):
    answer = n
    graph = [[] for _ in range(n+1)]
    
    # 송전탑의 트리 구조 입력
    for x, y in wires:
        graph[x].append(y)
        graph[y].append(x)

    # 송전탑의 전선을 하나씩 끊어보고 그 중 가장 차이가 적은 값 구하기
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
wires = [list(map(int, wire.split(","))) for wire in wires]
print(solution(n, wires))