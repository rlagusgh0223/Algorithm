from collections import deque

# 위치 찾는걸 알파벳 순서로 맞춰둬서
# 연산할때 따로 계산할 필요 없이 순서대로 계산하면
# 알파벳 순서대로 들어간다
dx = [1, 0, 0, -1]
dy = [0, -1, 1, 0]
w = ['d', 'l', 'r', 'u']

# 현재 위치부터 도착지까지 최단거리 반환하는 함수
def check(x, y, r, c):
    return abs(x-r) + abs(y-c)

# 최단거리-k가 짝수이면 목적지에 k번 보다 적게 도착해도
# 이전에 있던곳에 다시 갔다가 오는걸 반복하여
# k번에 맞춰 목적지에 도착할 수 있다
def solution(n, m, x, y, r, c, k):
    x, y, r, c = x-1, y-1, r-1, c-1

    # k가 도착까지 남은 거리보다 작다면 어차피 도착 못한다
    if check(x, y, r, c) > k:
        return 'impossible'
    
    q = deque()
    q.append((x, y, 0, ''))
    while q:
        x, y, cnt, road = q.popleft()
        # 목적지에 도착했는데 남은 이동수가 홀수면 도착 못한다
        if x==r and y==c and (k-cnt)%2:
            return 'impossible'
        # k번만큼 이동하여 목적지에 도착하면 이동 끝
        elif x==r and y==c and cnt==k:
            return road
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0<=nx<n and 0<=ny<m:
                # 다음 좌표에서 도착까지의 최단거리가
                # 남은 k의 수보다 크다면 갈 수 없으므로 다른 좌표 알아본다
                # 현재 cnt는 다음 좌표까지의 거리를 반영하지 않았으므로 cnt+1을 해준다
                if check(nx, ny, r, c) > k - (cnt+1):
                    continue
                q.append((nx, ny, cnt+1, road+w[i]))
                break


import sys

n, m, x, y, r, c, k = map(int, sys.stdin.readline().split())
print(solution(n, m, x, y, r, c, k))