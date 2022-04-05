import sys
while True:
    M, F = map(int, sys.stdin.readline().split())
    if M == 0 and F == 0:    # 0 0 을 입력하면 종료
        break
    print(M+F)    # 상근이의 모든 친구의 합