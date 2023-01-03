import sys
# 빠른 입력 함수 사용
input = sys.stdin.readline
from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 배열에서 N개의 원소를 선택하는 조합
def comb(arr, n):
    if n == 0:
        return [[]]
    result = []
    for i in range(len(arr)):
        front = arr[i]
        for back in comb(arr[i+1:], n-1):
            result.append([front]+back)
    return result

# 너비 우선 탐색(BFS)
def bfs(selected):
    global answer
    # 활성 바이러스(selected)들을 큐에 넣고 방문 처리
    visited = [[-1]*n for _ in range(n)]
    queue = deque()
    for (i, j) in selected:
        visited[i][j] = 0
        queue.append((i, j))
    cnt = 0  # 빈 공간을 바꾼 횟수
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if nx<0 or nx>=n or ny<0 or ny>=n:
                continue
            # 처음 방문하고, 벽이 아니면
            if visited[nx][ny]==-1 and arr[nx][ny]!=1:
                visited[nx][ny] = visited[x][y] + 1
                queue.append((nx, ny))
                if arr[nx][ny] == 0:  # 빈 공간
                    cnt += 1  # 빈 공간을 바꾼 횟수 세기
    taken = 0  # 최대 소요 시간
    for i in range(n):
        for j in range(n):
            # 비활성 바이러스는 처음부터 바이러스
            if arr[i][j] == 0:  # 빈 칸에 한해서만 소요 시간 계산
                taken = max(taken, visited[i][j])
    if cnt == target:
        answer = min(taken, answer)

# 연구소의 크기(n)와 바이러스의 개수(m) 입력
n, m = map(int, input().split())
# 바이러스 위치 정보
viruses = []
# 초기 연구소 맵 정보
arr = []
target = 0  # 빈 칸(퍼뜨려야 할 개수)
answer = int(1e9)  # 최종 정답
for i in range(n):
    arr.append(list(map(int, input().split())))
    for j in range(n):
        if arr[i][j] == 2:  # 바이러스인 경우
            viruses.append((i, j))
        if arr[i][j] == 0:  # 빈 칸인 경우
            target += 1

combinations = comb(viruses, m)
# 모든 활성 바이러스 조합(combination)에 대하여 BFS 수행
for selected in combinations:
    bfs(selected)
if answer == int(1e9):  # 바이러스를 모두 퍼뜨릴 수 없음
    print(-1)
else:
    print(answer)