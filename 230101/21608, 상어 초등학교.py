import sys
# 빠른 입력 함수 사용
input = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

n = int(input())  # 교실의 크기
# 전체 교실
arr = [[0]*n for _ in range(n)]
friends_dict = dict()

def allocate(id, friends):
    max_adj, max_cnt, max_x, max_y = [-1, -1, -1, -1]
    for x in range(n):
        for y in range(n):
            if arr[x][y] != 0:  # 이미 학생이 있으면 무시
                continue
            cnt, adj = [0, 0]
            for i in range(4):
                nx, ny = x+dx[i], y+dy[i]
                if nx<0 or nx>=n or ny<0 or ny>=n:
                    continue
                if arr[nx][ny] == 0:  # 비어있는 칸이라면
                    cnt += 1
                if arr[nx][ny] in friends:  # 좋아하는 학생이라면
                    adj += 1
            if adj > max_adj:  # 좋아하는 학생이 많이 인접한 곳으로
                max_adj, max_cnt, max_x, max_y = adj, cnt, x, y
            elif adj == max_adj:  # 여러 칸이라면
                if cnt > max_cnt:  # 주변에 비어있는 칸이 많은 곳으로
                    max_cnt, max_x, max_y = [cnt, x, y]
    arr[max_x][max_y] = id  # 적절한 위치에 학생 할당

# 한 명씩 학생의 정보를 입력받기
for i in range(n*n):
    row = list(map(int, input().split()))
    id = row[0]
    friends = row[1:]
    friends_dict[id] = friends
    # 교실에 학생 할당
    allocate(id, friends)

result = 0  # 전체 만족도의 합
for x in range(n):
    for y in range(n):
        number = 0
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if nx<0 or ny<0 or nx>=n or ny>=n:
                continue
            if arr[nx][ny] in friends_dict[arr[x][y]]:
                number += 1
        score = 0  # 현재 학생의 만족도
        if number == 1:
            score = 1
        if number == 2:
            score = 10
        if number == 3:
            score = 100
        if number == 4:
            score = 1000
        result += score
print(result)