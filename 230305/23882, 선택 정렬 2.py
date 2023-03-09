import sys
N, K = map(int, sys.stdin.readline().split())
lst = list(map(int, sys.stdin.readline().split()))
check = sorted(lst)
for i in range(N-1, 0, -1):  # 마지막에 남는 수는 어차피 가장 작은 수니까 계산할 필요 없다
    now = lst.index(check.pop())
    if lst[i] != lst[now]:
        lst[i], lst[now] = lst[now], lst[i]
        K -= 1
    if K == 0:
        print(*lst)
        exit()
print(-1)