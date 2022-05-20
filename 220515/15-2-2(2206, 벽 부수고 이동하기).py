# 모범답안을 보고 만든 내 코드를 3차원으로 만들었을뿐 다른건 없는것 같은데
# 이건 맞다고 하고 2차원으로 만든건 틀렸다고 한다
# 어차피 3차원으로 하는것도 wall을 이용해 벽을 부수었는지 부수지 않았는지 구분하기
# 위해서 인것 같은데 굳이 3차원으로 해야 되는 이유가 있나?

from collections import deque
import sys

dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]

def BFS():
    q = deque()
    q.append([0, 0, 0])    # 시작 위치와 아직 벽을 깨지 않았다는 표시 q에 입력
    visit = [[[0, 0] for _ in range(M)] for _ in range(N)]    # 방문한 경로의 거리를 저장하기 위한 배열
    visit[0][0][0] = 1    # (0,0)은 시작 위치이므로 1을 넣어준다
    while q:
        x, y, wall = q.popleft()    # 좌표와 벽을 깼는지 여부를 출력해서 변수에 넣어준다
        if x == N-1 and y == M-1:    # 만약 맵의 마지막까지 왔다면
            return visit[x][y][wall]    # visit에 입력된 거리 출력
        for i in range(4):    # 아니라면 사방 검색
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and visit[nx][ny][wall] == 0:    # 다음 경로가 맵 안에 있고 아직 방문하지 않았다면
                if map[nx][ny] == 0:    # map에서 다음 경로가 벽이 아니라면
                    visit[nx][ny][wall] = visit[x][y][wall] + 1    # visit의 다음경로에 현재경로+1의 값을 넣어준다
                    q.append([nx, ny, wall])    # 다음 경로와 벽을 깼는지의 유무를 전해준다
                if map[nx][ny] == 1 and wall == 0:    # map에서는 벽이라고 했으나 아직 벽을 깨지 않았다면
                    visit[nx][ny][1] = visit[x][y][0] + 1    # visit의 다음경로에 현재경로+1의 값을 넣어준다
                    q.append([nx, ny, 1])    # 다음 경로와 벽을 깼다는 표시를 q에 입력한다
    return -1

N, M = map(int, sys.stdin.readline().split())
map = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(N)]
print(BFS())




##################################################################
# 모범답안을 보고 만든 내 코드인데 뭐가 틀린건지 모르겠다
# from collections import deque
# import sys

# dx = [0, -1, 0, 1]
# dy = [-1, 0, 1, 0]

# def BFS():
#     q = deque()
#     q.append([0, 0, 0])    # 시작 위치와 아직 벽을 깨지 않았다는 표시 q에 입력
#     visit = [[0 for _ in range(M)] for _ in range(N)]    # 방문한 경로의 거리를 저장하기 위한 배열
#     visit[0][0] = 1    # (0,0)은 시작 위치이므로 1을 넣어준다
#     while q:
#         x, y, wall = q.popleft()    # 좌표와 벽을 깼는지 여부를 출력해서 변수에 넣어준다
#         if x == N-1 and y == M-1:    # 만약 맵의 마지막까지 왔다면
#             return visit[x][y]    # visit에 입력된 거리 출력
#         for i in range(4):    # 아니라면 사방 검색
#             nx = x + dx[i]
#             ny = y + dy[i]
#             if 0 <= nx < N and 0 <= ny < M and visit[nx][ny] == 0:    # 다음 경로가 맵 안에 있고 아직 방문하지 않았다면
#                 if map[nx][ny] == 0:    # map에서 다음 경로가 벽이 아니라면
#                     visit[nx][ny] = visit[x][y] + 1    # visit의 다음경로에 현재경로+1의 값을 넣어준다
#                     q.append([nx, ny, wall])    # 다음 경로와 벽을 깼는지의 유무를 전해준다
#                 if map[nx][ny] == 1 and wall == 0:    # map에서는 벽이라고 했으나 아직 벽을 깨지 않았다면
#                     visit[nx][ny] = visit[x][y] + 1    # visit의 다음경로에 현재경로+1의 값을 넣어준다
#                     q.append([nx, ny, 1])    # 다음 경로와 벽을 깼다는 표시를 q에 입력한다
#     return -1

# N, M = map(int, sys.stdin.readline().split())
# map = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(N)]
# print(BFS())





#############################################
# 모범답안
# wall이 0인 것과 벽을 부술 수 있는 상태인게 무슨 상관인지?
# 기존의 DFS문제와 크게 다를 것 없어 보이지만 많이 다른 것 같다
# 벽이 한개인 경우 부수고 가는데 그걸 어떻게 반영한건지 이해가 안된다
# 왜 visit[nx][ny][wall] = visit[x][y][wall] + 1 에서 wall값에 따라 값이 달라지는가?
# from collections import deque

# dx = [0, -1, 0, 1]
# dy = [-1, 0, 1, 0]

# def bfs():
#     visit = [[[0]*2 for _ in range(M)] for _ in range(N)]    # 해당 지점을 방문했는지, 벽을 부수었는지 저장하기 위한 배열 생성
#     visit[0][0][0] = 1    # 처음 위치(0,0)에 벽을 부수지 않은 상태로 방문했으므로 1로 값을 변경한다
    
#     while q:
#         x, y, wall = q.popleft()    # 큐의 좌표(x, y)와 벽의 상태를 받는다
#         if x==(N-1) and y==(M-1):    # x, y 가 목표지점(N-1, M-1)에 도착했다면 
#             return visit[x][y][wall]    # 최단거리가 몇인지 확인한다
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#             if 0<=nx<N and 0<=ny<M and visit[nx][ny][wall]==0:    # 이동할 칸이 맵 안이고, 다음에 이동할 칸을 방문하지 않았다면
#                 if Map[nx][ny] == 0:    # 이동할 칸의 맵이 0이 아니라면 벽을 부술 수 있는 위치가 아니므로
#                     visit[nx][ny][wall] = visit[x][y][wall] + 1    # 다음칸 이동거리, 벽을 부수지 않음 = 현재칸 이동거리+1, 벽을 부수지 않음 으로 설정
#                     q.append([nx, ny, wall])    # 큐에 다음 이동 칸과 현재 벽의 상태를 넣어준다
#                 if Map[nx][ny] == 1 and wall == 0:    # 이동할 칸의 맵이 1이고 벽을 부술 수 있는 상태라면(wall이 1이면 이미 한번 부순 것이므로 부술 수 없다)
#                     visit[nx][ny][1] = visit[x][y][0] + 1    # 다음 이동칸, 벽을 부숨 = 현재 칸 이동거리+1, 벽을 부수지 않음으로 설정
#                     q.append([nx, ny, 1])    # 큐에 다음 이동 칸과, 벽을 부순 상태를 넣어준다
#         for i in range(N):
#             print(visit[i])
#         print("---------------")
#     return -1    # 이동할 수 없는 경우에는 -1을 값으로 반환해준다

# N, M = map(int, input().split())
# Map = [list(map(int, input().rstrip())) for _ in range(N)]    # 맵을 입력 받는다
# q = deque()
# q.append([0, 0, 0])    # 큐에 좌표 (0,0)과 벽을 부수지 않은 상태인 0을 넣어준다
# print(bfs())