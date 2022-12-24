def go(x, y, direction):
    global ans
    if x==n-1 and y==n-1:
        return 1
    ans = 0
    if direction == 0:
        if y+1<n and a[x][y+1]==0:
            ans += go(x, y+1, 0)
        if x+1<n and y+1<n and a[x+1][y]==0 and a[x][y+1]==0 and a[x+1][y+1]==0:
            ans += go(x+1, y+1, 1)
    elif direction == 1:
        if y+1<n and a[x][y+1]==0:
            ans += go(x, y+1, 0)
        if x+1<n and y+1<n and a[x+1][y]==0 and a[x][y+1]==0 and a[x+1][y+1]==0:
            ans += go(x+1, y+1, 1)
        if x+1<n and a[x+1][y]==0:
            ans += go(x+1, y, 2)
    elif direction == 2:
        if x+1<n and y+1<n and a[x+1][y]==0 and a[x][y+1]==0 and a[x+1][y+1]==0:
            ans += go(x+1, y+1, 1)
        if x+1<n and a[x+1][y]==0:
            ans += go(x+1, y, 2)
    return ans

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
print(go(0, 1, 0))