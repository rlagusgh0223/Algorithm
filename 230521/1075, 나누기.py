import sys
N = int(sys.stdin.readline())
F = int(sys.stdin.readline())
N = (N // 100) * 100
for i in range(10):
    for j in range(10):  # 그냥 이거 대신 아예 위에서 100까지 반복문을 돌려도 된다
        if (N+i*10+j) % F == 0:
            print(i, j, sep='')
            exit()