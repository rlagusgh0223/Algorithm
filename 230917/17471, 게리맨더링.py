def BFS(nodes):
    q = deque()
    check = [0 for _ in range(N)]
    q.append(nodes[0])  # 입력된 tuple의 첫번째 값부터 시작한다
    check[nodes[0]] = 1
    while q:
        node = q.popleft()
        for i in range(len(arr[node])):  # 튜플의 길이만큼 반복
            if arr[node][i] == 0:  # 연결되어 있는 선거구가 아니면 제외
                continue
            if i not in nodes:  # 튜플에 있는 선거구가 아니면 제외
                continue
            if check[i] == 0:  # 방문한 적이 없는 곳이라면
                check[i] = 1
                q.append(i)
    return check.count(1) == len(nodes)  # 모든 지역을 방문했다면

def get_total(nodes):
    total = 0
    for node in nodes:
        total += people[node]
    return total


from itertools import combinations
from collections import deque
import sys
N = int(sys.stdin.readline())
people = list(map(int, sys.stdin.readline().split()))
arr = [[0 for _ in range(N)] for _ in range(N)]
for i in range(N):
    _, *dsts = map(int, sys.stdin.readline().split())  # 입력된 첫번째 변수는 _로 받고, 나머지는 dsts에 하나의 리스트로 packing된다
    for dst in dsts:
        arr[i][dst-1] = 1

X = {i for i in range(N)}
ans = int(1e9)
for i in range(1, N//2 + 1):  # A선거구에는 m, B선거구에는 N-m의 구역을 준다고 했을때 m의 범위를 <= N//2로 해야 중복을 피할 수 있다
    As = tuple(combinations(X, i))  # A선거구에 0<m<=n/2개의 구역을 할당하는 경우 조합, X에서 i의 길이만큼 뽑아낸 후 tuple로 만든다
    for A in As:  # i의 길이만큼 있는 tuple들을 각각 비교
        B = list(X.difference(A))  # 집합자료형의 차집합, A의 tuple에 없는 선거구들을 리스트로 묶음
        if BFS(A) and BFS(B):  # A와 B구역이 적절하게 나뉘어 졌다면
            a = get_total(A)
            b = get_total(B)
            ans = min(ans, abs(a - b))

if ans == int(1e9):
    print(-1)
else:
    print(ans)