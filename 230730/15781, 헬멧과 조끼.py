import sys
N, M = map(int, sys.stdin.readline().split())
h = list(map(int, sys.stdin.readline().split()))
a = list(map(int, sys.stdin.readline().split()))
print(max(h) + max(a))