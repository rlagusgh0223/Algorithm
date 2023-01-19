import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    N = int(input())
    X = list(map(int, input().split()))
    for i in range(1, N):
        X[i] = max(X[i-1]+X[i], X[i])
    print(max(X))