import sys
N = sys.stdin.readline().rstrip()
n = len(N)
ck = []
for i in range(1, n-2):
    for j in range(i+1, n):
        now = N[:i][::-1] + N[i:j][::-1] + N[j:][::-1]
        ck.append(now)
print(min(ck))