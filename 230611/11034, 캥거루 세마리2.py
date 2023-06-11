import sys
while True:
    try:
        A, B, C = map(int, sys.stdin.readline().split())
        print(max(B-A-1, C-B-1))  # 차의 결과 1은 있어야 중간에 들어갈 수 있다
    except:
        break