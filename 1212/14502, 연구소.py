from collections import deque
import sys

N, M = map(int, sys.stdin.readline().split())
graph = [0] * N
for i in range(N):
    graph[i] = list(map(int, sys.stdin.readline().split()))

for i in range(N):
    print(graph[i])