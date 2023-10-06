import sys
ground = [list(sys.stdin.readline().strip()) for _ in range(8)]
start = 1
cnt = 0
for i in range(8):
    start = (start+1) % 2
    for j in range(start, 8, 2):
        if ground[i][j] == 'F':
            cnt += 1
print(cnt)