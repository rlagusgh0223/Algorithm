N = int(input())
A = [int(now) for now in input().split()]
chk = [1] * N

for i in range(N):
  for j in range(i):
    if A[i] > A[j] and chk[i] <= chk[j]:
      chk[i] = chk[j]+1

print(max(chk))