import sys

def divide(x, y, n):
    global white, blue
    samecolor = paper[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if samecolor != paper[i][j]:
                divide(x, y, n//2)
                divide(x, y+n//2, n//2)
                divide(x+n//2, y, n//2)
                divide(x+n//2, y+n//2, n//2)
                return
    if samecolor == 0:
        white += 1
        return
    else:
        blue += 1
        return

N = int(sys.stdin.readline())
paper = [[int(x) for x in sys.stdin.readline().split()] for _ in range(N)]

white = blue = 0
divide(0, 0, N)
print(white)
print(blue)