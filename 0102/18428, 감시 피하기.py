from collections import deque
import sys

graph = []
t = []
s = []
endFlag = False
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
N = int(sys.stdin.readline())

for i in range(N):
    graph.append(list(sys.stdin.readline().split()))
    for j in range(len(graph[i])):
        if graph[i][j] == 'T':
            t.append([i,j])
        elif graph[i][j] == 'S':
            s.append([i,j])

for x, y in t:
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < N:
            if graph[nx][ny] == 'S':
                endFlag = True
                break
    if endFlag:
        break

for T in range(len(t)):
    for S in range(len(s)):
        if t[T][0] == s[S][0]:
            X = (T+S) // 2
            Y = t[T][0]
            if graph[X][Y] == 'X':
                graph[X][Y] = 'O'
        if t[T][1] == s[S][1]:
            X = (T+S) // 2
            Y = t[T][1]
            if graph[X][Y] == 'X':
                graph[X][Y] = 'O'

for i in range(N):
    print(graph[i])
if endFlag:
    print("NO")
else:
    print("YES")
