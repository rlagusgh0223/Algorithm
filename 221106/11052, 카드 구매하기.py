import sys
N = int(sys.stdin.readline())
P = [0] + list(map(int, sys.stdin.readline().split()))
D = [0] * (N+1)
for i in range(1, N+1):
    for j in range(1, i+1):
        # i개의 카드를 구매할땐 i-j개의 카드와 j번째 카드팩을 구매한다
        D[i] = max(D[i], D[i-j]+P[j])
print(D[N])