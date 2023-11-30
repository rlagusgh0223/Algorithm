from collections import deque
def BFS(start, n, graph):
    q = deque()
    q.append(start)
    # 카운트한 적이 있는지 체크하기 위한 리스트
    visit = [0] * (n+1)
    visit[start] = 1
    # 연결되어 있는 모든 송전탑의 개수
    cnt = 0
    while q:
        now = q.popleft()
        # 현재 송전탑에서 연결된 모든 송전탑 체크
        for i in graph[now]:
            if visit[i] == 0: 
                visit[i] = 1
                cnt += 1
                q.append(i)
    return cnt

def solution(n, wires):
    answer = n
    # 서로간에 연결된걸 표시하기 위한 리스트
    graph = [[] for _ in range(n+1)]
    # 입력받은 송전탑 graph상에서 연결하기
    for a, b in wires:
        graph[a].append(b)
        graph[b].append(a)
    # 입력받은 송전탑의 연결 중 하나를 끊고 이어진 송전탑의 개수 차이 비교한 후 다시 연결하기
    for a, b in wires:
        graph[a].remove(b)
        graph[b].remove(a)
        answer = min(answer, abs(BFS(a, n, graph) - BFS(b, n, graph)))
        graph[a].append(b)
        graph[b].append(a)
    return answer

import sys
n = int(sys.stdin.readline())
wires = list(sys.stdin.readline().strip().split("],["))
wires = [list(map(int, w.split(","))) for w in wires]
print(solution(n, wires))