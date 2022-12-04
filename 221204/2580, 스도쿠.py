def square(x, y):
    return (x//3)*3 + (y//3)

def go(z):
    if z == 81:
        for row in a:
            print(' '.join(map(str, row)))
        return True
    x = z//n
    y = z%n
    if a[x][y] != 0:
        return go(z+1)
    else:
        for i in range(1, 10):
            if c[x][i]==False and c2[y][i]==False and c3[square(x,y)][i]==False:
                c[x][i] = c2[y][i] = c3[square(x,y)][i] = True
                a[x][y] = i
                if go(z+1):
                    return True
                c[x][i] = c2[y][i] = c3[square(x,y)][i] = False
                a[x][y] = 0
    return False

n = 9
a = [list(map(int, input().split())) for _ in range(n)]
c = [[False]*10 for _ in range(n)]
c2 = [[False]*10 for _ in range(n)]
c3 = [[False]*10 for _ in range(n)]
for i in range(n):
    for j in range(n):
        if a[i][j] != 0:
            c[i][a[i][j]] = True
            c2[j][a[i][j]] = True
            c3[square(i,j)][a[i][j]] = True
go(0)