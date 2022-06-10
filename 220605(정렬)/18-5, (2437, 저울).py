import sys
n = int(sys.stdin.readline())
weight = [now for now in map(int, sys.stdin.readline().split())]
weight.sort()
num = 1

for i in weight:
    if num < i:
        break
    num += i

print(num)