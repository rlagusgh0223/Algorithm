import sys
input = sys.stdin.readline

# 맵의 크기(N), 파이어볼의 수(M), 이동 명령 수(K)
N, M, K = map(int, input().split())

# 초기 모든 파이어볼 정보 입력
balls = []
for i in range(M):
    x, y, m, s, d = map(int, input().split())
    balls.append((x-1, y-1, m, s, d))

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

# 모든 파이어볼을 이동하는 함수
def move():
    # N X N 맵의 어느 위치에 몇 개의 파이어볼이 있는지 표현
    arr = [[[] for _ in range(N)] for _ in range(N)]
    # 모든 파이어볼이 자신의 방향(d)으로 속력(s)만큼 이동
    for i in range(len(balls)):
        x, y, m, s, d = balls[i]
        x = (x+dx[d]*s) % N
        y = (y+dy[d]*s) % N
        arr[x][y].append((m, s, d))  # (질량, 속력, 방향)
        balls[i] = (x, y, m, s, d)  # 파이어볼 이동
    return arr  # 이동 결과 배열

def split():  # 2개 이상의 파이어볼이 잇는 칸에서 파이어볼을 분할하는 함수
    new_balls = []  # 분할되어 새롭게 추가된 파이어볼들
    removed = set()  # 분할되면서 제거된 파이어볼 위치들
    for i in range(N):
        for j in range(N):
            if len(arr[i][j]) >= 2:  # 2개 이상의 파이어볼이 있는 칸이라면
                removed.add((i, j))
                sum_m = 0  # 질량의 합
                sum_s = 0  # 속력의 합
                even = True  # 전부 짝수인지 여부
                odd = True  # 전부 홀수인지 여부
                for (m, s, d) in arr[i][j]:  # 해당 위치에 있는 모든 파이어볼을 확인하며
                    sum_m += m
                    sum_s += s
                    if d%2 == 0:
                        odd = False
                    if d%2 == 1:
                        even = False
                # 해당 위치의 모든 파이어볼이 일관적으로 짝수/홀수인지 확인
                if odd or even:
                    directions = [0, 2, 4, 6]
                else:
                    directions = [1, 3, 5, 7]
                for d in directions :  # 각 방향으로 이동하는 파이어볼 4개로 분할
                    if sum_m//5 > 0:  # 질량이 존재할 때만 추가하기
                        ball = (i, j, sum_m//5, sum_s//len(arr[i][j]), d)
                        new_balls.append(ball)
    return removed, new_balls

for _ in range(K):
    arr = move()  # 모든 파이어볼 이동
    # 2개 이상 모인 파이어볼 쪼개기
    removed, new_balls = split()
    for ball in balls:
        x, y = ball[:2]
        # 분할되면서 제거된 파이어볼들을 제외하기
        if (x, y) not in removed:
            new_balls.append(ball)
    balls = new_balls

# 정답 출력하기
answer = 0
for ball in balls:
    answer += ball[2]
print(answer)