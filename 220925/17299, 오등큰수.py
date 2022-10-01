import sys
N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
NGF = [-1] * N
F = [0] * 1000001
stack = []
for i in A:
    F[i] += 1

for now in range(N):
    while stack and F[A[stack[-1]]] < F[A[now]]:
        NGF[stack.pop()] = A[now]
    stack.append(now)

for i in range(len(NGF)-1):
    print(NGF[i], end=' ')
print(NGF[-1])