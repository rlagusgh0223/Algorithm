import sys
T = int(sys.stdin.readline())
answer = [0] * T
for i in range(T):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    n = int(sys.stdin.readline())
    for j in range(n):
        X, Y, r = map(int, sys.stdin.readline().split())
        d1 = ((x1-X)**2 + (y1-Y)**2)**0.5
        d2 = ((x2-X)**2 + (y2-Y)**2)**0.5
        if (d1>r and d2<r) or (d1<r and d2>r):
            answer[i] += 1
for now in answer:
    print(now)