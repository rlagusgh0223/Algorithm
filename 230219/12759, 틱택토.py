import sys
s = int(sys.stdin.readline())
lst = [[0]*3 for _ in range(3)]
ans = 0
for _ in range(9):
    x, y = map(int, sys.stdin.readline().split())
    lst[x-1][y-1] = s
    s = s%2+1
    if ans == 0:
        for i in range(3):
            if lst[i][0]==lst[i][1]==lst[i][2]:
                ans = lst[i][0]
            if lst[0][i]==lst[1][i]==lst[2][i]:
                ans = lst[0][i]
        if lst[0][0]==lst[1][1]==lst[2][2] or lst[0][2]==lst[1][1]==lst[2][0]:
            ans = lst[1][1]
print(ans)