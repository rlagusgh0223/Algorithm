import sys
T = int(sys.stdin.readline())
for _ in range(T):
    n = int(sys.stdin.readline())
    lst = [[1 for _ in range(10)]] + [[0]*10 for _ in range(n-1)]
    for i in range(1, n):
        lst[i][0] = sum(lst[i-1])
        for j in range(1, 10):
            lst[i][j] = lst[i][j-1] - lst[i-1][j-1]
    print(sum(lst[n-1]))