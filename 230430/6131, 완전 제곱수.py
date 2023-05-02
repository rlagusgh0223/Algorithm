import sys
N = int(sys.stdin.readline())
cnt = 0
for i in range(1, 501):
    for j in range(1, i+1):
        if i**2 - N == j**2:
            cnt += 1
print(cnt)