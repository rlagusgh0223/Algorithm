import sys
N, S = map(int, sys.stdin.readline().split())
a = list(map(int, sys.stdin.readline().split()))
ans = 0
for i in range(1, (1<<N)):  # 1부터 전체가 1이 N개 있는 전체집합((1<<N)-1 이 전체집합인데 어차피 마지막수는 계산 안하니 1<<N으로 표현)까지(양수라고 했으므로 공집합인 0은 제외)
    s = sum(a[k] for k in range(N) if (i&(1<<k)))  # 0부터 N-1까지 비트마스크 i에 k가 들어있는지
    if S == s:
        ans += 1
print(ans)