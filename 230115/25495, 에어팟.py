import sys
N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
result = 2  # 중첩된 소모량
now = 2  # 이번 소모량
for i in range(1, N):
    if result!=0 and A[i] == A[i-1]:
        now *= 2
    else:
        now = 2
    result += now
    if result >= 100:
        result = 0
print(result)