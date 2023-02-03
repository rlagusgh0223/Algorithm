import sys
R, C, ZR,ZC = map(int, sys.stdin.readline().split())
en = [list(sys.stdin.readline().rstrip()) for _ in range(R)]
lst = [[en[i//ZR][j//ZC] for j in range(C*ZC)] for i in range(R*ZR)]
for i in range(R*ZR):
    print(*lst[i], sep='')