import sys
n = int(sys.stdin.readline())
wine = [0] * (n+1)
for i in range(n):
  wine[i] = int(sys.stdin.readline().rstrip())
chk = [0]
chk.append(wine[0])
chk.append(wine[0]+wine[1])

for i in range(3, n+1):
  chk.append(max(chk[i-1], wine[i-1]+chk[i-2], wine[i-1]+wine[i-2]+chk[i-3]))

print(max(chk))