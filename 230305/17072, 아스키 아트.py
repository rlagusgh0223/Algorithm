import sys
N, M = map(int, sys.stdin.readline().split())
RGB = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
ans = [[0]*M for _ in range(N)]
for i in range(N):
    for j in range(0, M*3, 3):
        now = 2126*RGB[i][j] + 7152*RGB[i][j+1] + 722*RGB[i][j+2]
        if 0 <= now < 510000:
            ans[i][j//3] = '#'
        elif 510000 <= now < 1020000:
            ans[i][j//3] = 'o'
        elif 1020000 <= now < 1530000:
            ans[i][j//3] = '+'
        elif 1530000 <= now < 2040000:
            ans[i][j//3] = '-'
        else:
            ans[i][j//3] = '.'
for i in range(N):
    print(''.join(ans[i]))