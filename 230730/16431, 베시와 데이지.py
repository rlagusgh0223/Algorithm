import sys
Br, Bc = map(int, sys.stdin.readline().split())
Dr, Dc = map(int, sys.stdin.readline().split())
Jr, Jc = map(int, sys.stdin.readline().split())
# 베시는 대각선으로 이동 가능하므로 x축과 y축 이동 중 큰값을 준다
B = max(abs(Jr - Br), abs(Jc - Bc))
# 데이지는 대각선으로 이동할 수 없으므로 x축과 y축 이동을 더한다
D = abs(Jr - Dr) + abs(Jc - Dc)

if B == D:
    print("tie")
elif B < D:
    print("bessie")
else:
    print("daisy")