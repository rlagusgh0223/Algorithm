import sys
while True:
    B, N = map(int, sys.stdin.readline().split())
    if B == N == 0:
        break
    A = 0
    # 우선 N제곱을 했을때 처음 B보다 큰 수(A)를 찾는다(이 A나 A-1이 B와 가장 가까운 값이다)
    while A**N < B:
        A += 1
    # B와 값의 차이가 더 작은 값을 찾는다
    # B와 A**N의 값의 차가 더 적다면 A를 출력하고
    # B와 (A-1)**N의 값의 차가 더 적다면 A-1을 출력한다
    # 둘의 값이 같은 경우에는 A나 A-1 중 어느 값을 출력해도 상관없다
    if abs(B - A**N) < abs(B - (A-1)**N):
        print(A)
    else:
        print(A-1)