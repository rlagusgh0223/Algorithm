N = int(input())
S = list(map(int, input().split()))
c = [False] * (N*100000 + 10)
for i in range(1<<N):
    s = 0
    for j in range(N):
        if i & (1<<j):
            s += S[j]
    c[s] = True
i = 1
while True:
    if c[i] == False:
        break
    i += 1
print(i)