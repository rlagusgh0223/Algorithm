import sys
input = sys.stdin.readline

n, m = map(int, input().split())
# 초기 구름은 맵의 가장 왼쪽 아래에서 4칸을 차지
clouds = [(n-1, 0), (n-1, 1), (n-2, 0), (n-2, 1)]

dx = [0, -1, -1, -1, 0, 1, 1, 1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]

arr = []
# N X N 맵 정보 입력(물의 수)
for i in range(n):
    arr.append(list(map(int, input().split())))

# 구름을 이동한 뒤에 비가 내리도록 하는 함수
def rain(d, s):
    positions = []  # 물이 증가한 칸들
    for cloud in clouds:
        x, y = cloud  # 현재 구름의 위치(x, y)
        # 현재의 방향으로 s번 이동(위치는 순환) 
        x = (x+dx[d-1]*s) % n
        y = (y+dy[d-1]*s) % n
        arr[x][y] += 1  # 이동한 뒤에 비 내리기
        positions.append((x, y))
    return positions

for _ in range(m):  # M번의 연산을 차례대로 확인
    d, s = map(int, input().split())  # 방향(d)과 이동 횟수(s)
    positions = rain(d, s)  # 구름 이동 및 비 내리기
    # 비(구름)가 내린 모든 위치에 대하여, 대각선 방향을 확인해 덧셈
    for position in positions:
        x, y = position
        cnt = 0  # 대각선으로 인접한 위치 중에서 물이 있는 개수
        # 대각선 방향(1, 3, 5, 7)만 확인
        for i in range(1, 8, 2):
            nx, ny = x+dx[i], y+dy[i]
            # 범위를 벗어나는 경우 무시
            if nx<0 or ny<0 or nx>=n or ny>=n:
                continue
            # 인접한 위치에 물이 있다면 카운트
            if arr[nx][ny] >= 1:
                cnt += 1
        arr[x][y] += cnt
    positions = set(positions)  # 비가 내린 부분에는 새로운 구름 안 생김
    clouds = []  # 새로운 구름 초기화
    for i in range(n):
        for j in range(n):
            # 값이 2 이상이고, 기존에 구름이 없던 위치에 새로운 구름 생성
            if arr[i][j]>=2 and (i,j) not in positions:
                clouds.append((i, j))
                arr[i][j] -= 2

# 정답 출력
answer = 0
for row in arr:
    answer += sum(row)
print(answer)