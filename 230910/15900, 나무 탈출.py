# pypy3로 해야된다
import sys
sys.setrecursionlimit(10**5)  #자꾸 런타임에러(RecursiontError) 뜨는데 이것때문인것 같다. 그렇다고 6으로 늘리면 메모리 초과 떠서 안딘다
# 인터넷의 정답 코드도 틀렸다고 하는거 봐서 문제가 또 바뀌었나 보다
def DFS(now):
    visit[now] = True
    for nxt in graph[now]:
        if visit[nxt] == False:
            distance[nxt] = distance[now] + 1
            DFS(nxt)

N = int(sys.stdin.readline())
answer = 0
visit = [False for _ in range(N+1)]
graph = [[] for _ in range(N+1)]
distance = [0 for _ in range(N+1)]
for i in range(N-1):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)
DFS(1)
# 편의를 위해 0은 만들기만 하고 사용하지 않으며, 루트노드는 1번부터 시작한다. 2번부터 리프노드를 찾는다(연결이 하나뿐인 노드)
for i in range(2, N+1):
    if len(graph[i]) == 1:
        answer += distance[i]
if answer % 2 == 0:
    print("No")
else:
    print("Yes")