import sys
# 여기서 한 칸 오른쪽은 0->1이 아닌, A->B이므로 x자리를 바꿔주는게 맞다
move = {'R': [1, 0], 'L': [-1, 0], 'B': [0, -1], 'T': [0, 1], 'RT': [1, 1], 'LT': [-1, 1], 'RB': [1, -1], 'LB': [-1, -1]}

king, stone, N = sys.stdin.readline().split()
k = list(map(int, [ord(king[0])-64, king[1]]))
s = list(map(int, [ord(stone[0])-64, stone[1]]))
for _ in range(int(N)):
    m = sys.stdin.readline().rstrip()
    nx = k[0] + move[m][0]
    ny = k[1] + move[m][1]
    if 0<nx<=8 and 0<ny<=8:
        if nx==s[0] and ny==s[1]:
            sx = s[0] + move[m][0]
            sy = s[1] + move[m][1]
            if 0<sx<=8 and 0<sy<=8:
                k = [nx, ny]
                s = [sx, sy]
        else:
            k = [nx, ny]  # 어차피 k=[nx, ny]라 먼저 해도 될 것 같은데 안된다고 한다
k[0], s[0] = chr(k[0]+64), chr(s[0]+64)
print(*k, sep='')
print(*s, sep='')