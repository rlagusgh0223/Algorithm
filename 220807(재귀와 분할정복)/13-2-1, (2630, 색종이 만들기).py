import sys

def divide(x, y, N):
    global white, blue
    samecolor = paper[x][y]
    for i in range(x, x+N):
        for j in range(y, y+N):
            if samecolor != paper[i][j]:
                divide(x, y, N//2)
                divide(x, y+N//2, N//2)
                divide(x+N//2, y, N//2)
                divide(x+N//2, y+N//2, N//2)
                return
    if samecolor == 0:
        white += 1
        return
    else:
        blue += 1
        return

N = int(sys.stdin.readline())
paper = [[int(x) for x in sys.stdin.readline().split()] for _ in range(N)]
white = 0
blue = 0

divide(0, 0, N)
print(white)
print(blue)