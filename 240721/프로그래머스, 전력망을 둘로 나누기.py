from collections import deque


# BFS를 이용해서 해당 송전탑에 연결된 송전탑의 개수를 구한다
def BFS(start, n, graph):
    q = deque()
    visit = [0] * (n+1)
    visit[start] = 1
    q.append(start)
    cnt = 0
    while q:
        x = q.popleft()
        for i in graph[x]:
            if visit[i] == 0:
                cnt += 1
                visit[i] = 1
                q.append(i)
    return cnt


def solution(n, wires):
    answer = 100
    # 각 송전탑 별로 연결된 송전탑을 기록할 리스트
    graph = [[] for _ in range(n+1)]

    # 각 송전탑이 연결된 송전탑 입력
    for a, b in wires:
        graph[a].append(b)
        graph[b].append(a)
    
    # 송전탑 연결 중 한 곳을 끊었을때 두 전력망의 송전탑 개수의 차이 비교
    # 끊은 후 다시 연결해서 다음 계산에 지장 없게 한다
    for a, b in wires:
        graph[a].remove(b)
        graph[b].remove(a)
        answer = min(answer, abs(BFS(a, n, graph) - BFS(b, n, graph)))
        graph[a].append(b)
        graph[b].append(a)

    return answer

import sys

n = int(sys.stdin.readline())
wires = list(sys.stdin.readline().strip().split('],['))
wires = [list(map(int, w.split(","))) for w in wires]
print(solution(n, wires))