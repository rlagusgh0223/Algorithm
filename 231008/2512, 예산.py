import sys
N = int(sys.stdin.readline())
n = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
start, end = 0, max(n)
while start <= end:
    mid = (start + end) // 2
    total = 0
    for now in n:
        if now > mid:
            total += mid
        else:
            total += now
    if total <= M:
        start = mid + 1
    else:
        end = mid - 1
print(end)