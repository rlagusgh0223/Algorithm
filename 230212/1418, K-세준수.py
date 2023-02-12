import sys
N = int(sys.stdin.readline())
K = int(sys.stdin.readline())
s = [0 for i in range(N+1)]
for i in range(2, N+1):
    if s[i] == 0:
        for t in range(i, N+1, i):
            s[t] = i
cnt = 0
for i in s[1:]:
    if i <= K:
        cnt += 1
print(cnt)