import sys
N = int(sys.stdin.readline())
lst = [int(sys.stdin.readline()) for _ in range(N)]
lst.sort(reverse=True)
for l in lst:
    print(l)