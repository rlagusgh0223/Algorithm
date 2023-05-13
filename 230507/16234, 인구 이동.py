def BFS():  # 여기에 human, L, R 넣는거 조금 더 빠르기는 한데 드라마틱하게 빠른것도 아니고 굳이 그럴 필요가 있나 싶어서 안 넣었다
    ok = False  # 인구 이동이 일어났는지 반영하는 변수
    ck = [[0]*N for _ in range(N)]  # 인구 점검한 나라인지 체크할 리스트
    for i in range(N):  # 모든 나라를 본다
        for j in range(N):
            if ck[i][j] == 0:  # 점검한 적이 없는 나라라면
                ck[i][j] = 1  # 점검했다고 표시하고
                q = deque()
                q.append((i, j))  # 큐에 현재 나라의 좌표 넣어준다
                move = [(i, j)]  # 인구 이동할 나라의 리스트에 현재 나라의 좌표 넣어준다
                total = human[i][j]  # 인구 이동할 나라의 총 인구수에 현재 나라의 인구 추가한다
                while q:
                    x, y = q.popleft()
                    for k in range(4):
                        nx, ny = x+dx[k], y+dy[k]
                        # 다음 좌표가 리스트 안에 있고 방문한 적 없는 국가이며 인구 이동이 가능한 인구차라면
                        if 0<=nx<N and 0<=ny<N and ck[nx][ny]==0 and L<=abs(human[nx][ny]-human[x][y])<=R:
                            ck[nx][ny] = 1  # 점검했다고 체크하고
                            q.append((nx, ny))  # 큐와 이동할 나라 리스트에 좌표 추가한다
                            move.append((nx, ny))
                            total += human[nx][ny]  # 이동할 나라들의 총 인구수에 다음 나라 인구 추가
                            ok = True  # 인구이동이 일어났으므로 이동했다고 변수 입력
                # 각 나라에 살 평균 인구를 구하고 입력한다
                total //= len(move)
                for x, y in move:
                    human[x][y] = total
    return ok

from collections import deque
import sys
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
N, L, R = map(int, sys.stdin.readline().split())
human = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
ans = 0  # 인구 이동이 일어나는 날 저장하는 변수
while BFS():  # 인구 이동이 일어났다면
    ans += 1  # 날짜 하루 증가
print(ans)