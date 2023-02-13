# 버린다는 말은 신경쓸거 없다
# 그냥 1번부터 M번까지의 카드를 나눠주는걸 M번 반복하면 된다
# 나눠주는 카드의 현재 번호를 i로 주는거다
# 이때 나머지 값이 앞의 수가 더 크면 바꿔준다
import sys
N, M = map(int, sys.stdin.readline().split())
A = [int(sys.stdin.readline()) for _ in range(N)]
for i in range(1, M+1):
    for j in range(N-1):
        if A[j]%i > A[j+1]%i:
            A[j], A[j+1] = A[j+1], A[j]
print(*A, sep='\n')