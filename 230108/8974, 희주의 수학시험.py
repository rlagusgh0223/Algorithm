import sys
A, B = map(int, sys.stdin.readline().split())
lst = []
now = 1
cnt = 0
for i in range(B):
    cnt += 1
    lst.append(now)
    if now == cnt:
        now += 1
        cnt = 0
print(sum(lst[A-1:B]))