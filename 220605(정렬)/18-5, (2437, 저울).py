import sys
N = int(sys.stdin.readline())
weight = list(map(int, sys.stdin.readline().split()))

weight.sort()
num = 1

for now in weight:
    if num < now:
        break
    num += now

print(num)