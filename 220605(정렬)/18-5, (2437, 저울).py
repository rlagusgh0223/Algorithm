import sys
N = int(sys.stdin.readline())
lst = [int(now) for now in sys.stdin.readline().split()]
lst.sort()
num = 1

for i in lst:
    if num < i:
        break
    num += i

print(num)