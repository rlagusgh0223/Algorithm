n = int(input())
drink = [0] * (n+1)
for i in range(n):
  drink[i] = int(input())

chk = [0]
chk.append(drink[0])
chk.append(drink[0] + drink[1])

for i in range(3, n+1):
  chk.append(max(chk[i-1], drink[i-1]+chk[i-2], drink[i-1]+drink[i-2]+chk[i-3]))

print(chk[n])