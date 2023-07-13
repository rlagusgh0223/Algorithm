import sys
num = []
for i in range(7):
    now = int(sys.stdin.readline())
    if now % 2 == 1:
        num.append(now)
if num:
    print(sum(num))
    print(min(num))
else:
    print(-1)