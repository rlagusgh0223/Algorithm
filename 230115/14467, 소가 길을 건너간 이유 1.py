import sys
N = int(sys.stdin.readline())
cow = [-1] * 11
cnt = 0
for _ in range(N):
    x, y = map(int, sys.stdin.readline().split())
    if cow[x] == -1:  # 최초 관측된 경우
        cow[x] = y
    elif cow[x] != y:  # 이전 관측된 위치와 바뀐 경우
        cow[x] = y
        cnt += 1
    # 이전 관측된 위치와 똑같으면 바꾸지 않아도 된다
print(cnt)