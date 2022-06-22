n = int(input())
wine = [0] * (n+1)
for i in range(n):
  wine[i] = int(input())
overlap = [0]
overlap.append(wine[0])
overlap.append(wine[0]+wine[1])

for i in range(3, n+1):
  overlap.append(max(overlap[i-1], wine[i-1]+overlap[i-2], wine[i-1]+wine[i-2]+overlap[i-3]))

print(overlap[n])