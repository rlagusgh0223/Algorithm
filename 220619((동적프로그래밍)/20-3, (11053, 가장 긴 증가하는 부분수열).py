import sys
A = int(sys.stdin.readline())
AI = [int(now) for now in sys.stdin.readline().split()]

D = [1] * A

for i in range(A):
  for j in range(i):
    if AI[i] > AI[j] and D[i] <= D[j]:
      D[i] = D[j]+1

print(max(D))