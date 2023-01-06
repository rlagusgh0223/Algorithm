import sys
input = sys.stdin.readline
M = int(input())
A = [0, 1, 0, 0]
for i in range(M):
    X, Y = map(int, input().split())
    A[X], A[Y] = A[Y], A[X]
print(A.index(1))  # index : 배열에서 1이 있는 곳의 위치 출력