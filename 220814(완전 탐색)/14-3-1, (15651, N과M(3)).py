def DFS(depth):
    if depth == M:
        print(' '.join(map(str, answer)))
        return
    for i in range(1, N+1):
        answer.append(i)
        DFS(depth+1)
        answer.pop()

N, M = map(int, input().split())
answer = []
DFS(0)