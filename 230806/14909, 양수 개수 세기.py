import sys
num = list(map(int, sys.stdin.readline().split()))
n = 0
for now in num:
    if now > 0:
        n += 1
print(n)