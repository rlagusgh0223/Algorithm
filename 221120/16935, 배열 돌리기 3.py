def op1(lst):
    n = len(lst)
    m = len(lst[0])
    ans = [[0]*m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            ans[i][j] = lst[n-i-1][j]
    return ans

def op2(lst):
    n = len(lst)
    m = len(lst[0])
    ans = [[0]*m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            ans[i][j] = lst[i][m-j-1]
    return ans

def op3(lst):
    n = len(lst)
    m = len(lst[0])
    ans = [[0]*n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            ans[i][j] = lst[n-j-1][i]
    return ans

def op4(lst):
    n = len(lst)
    m = len(lst[0])
    ans = [[0]*n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            ans[i][j] = lst[j][m-i-1]
    return ans

def op5(lst):
    n = len(lst)
    m = len(lst[0])
    ans = [[0]*m for _ in range(n)]
    for i in range(n//2):
        for j in range(m//2):
            ans[i][j] = lst[i+n//2][j]
            ans[i][j+m//2] = lst[i][j]
            ans[i+n//2][j+m//2] = lst[i][j+m//2]
            ans[i+n//2][j] = lst[i+n//2][j+m//2]
    return ans

def op6(lst):
    n = len(lst)
    m = len(lst[0])
    ans = [[0]*m for _ in range(n)]
    for i in range(n//2):
        for j in range(m//2):
            ans[i][j] = lst[i][j+m//2]
            ans[i][j+m//2] = lst[i+n//2][j+m//2]
            ans[i+n//2][j+m//2] = lst[i+n//2][j]
            ans[i+n//2][j] = lst[i][j]
    return ans

import sys
N, M, R = map(int, sys.stdin.readline().split())
lst = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
func = [op1, op2, op3, op4, op5, op6]
for op in map(int, sys.stdin.readline().split()):
    lst = func[op-1](lst)
for row in lst:
    print(*row, sep=' ')