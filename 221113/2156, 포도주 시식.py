import sys
n = int(sys.stdin.readline())
A = [0]
for i in range(n):
    A.append(int(sys.stdin.readline()))
D = [0] * (n+1)
D[1] = A[1]
if n >= 2:
    D[2] = A[1] + A[2]
for i in range(3, n+1):
    D[i] = D[i-1]  # 이번 잔을 안마시는 경우
    if D[i] < D[i-2] + A[i]:  # 이번 잔과 그 앞앞 잔을 마시는 경우
        D[i] = D[i-2] + A[i]
    if D[i] < D[i-3] + A[i] + A[i-1]:  # 이번 잔과 그 앞 잔을 마시는 경우
        D[i] = D[i-3] + A[i] + A[i-1]
print(D[n])