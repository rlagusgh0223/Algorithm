import sys
N, K = map(int, sys.stdin.readline().split())
temp = list(map(int, sys.stdin.readline().split()))
ck = []
for i in range(N-K+1):
    ans = 0
    for j in range(i, i+K):
        ans += temp[j]
    ck.append(ans)
print(max(ck))