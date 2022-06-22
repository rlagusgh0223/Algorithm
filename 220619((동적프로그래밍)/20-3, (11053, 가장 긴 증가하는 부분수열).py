import sys
n = int(sys.stdin.readline())
A = [int(num) for num in map(int, sys.stdin.readline().split())]
chk = [1] * n

for i in range(n):
  for j in range(i):
    if A[i]>A[j] and chk[i]<=chk[j]:
      chk[i] = chk[j]+1

print(max(chk))