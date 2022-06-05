import sys
N = int(sys.stdin.readline())
lst = list(map(int, sys.stdin.readline().split()))
lst.sort()

num = 1
for i in range(N):
    if num < lst[i]:
        break
    num += lst[i]

print(num)