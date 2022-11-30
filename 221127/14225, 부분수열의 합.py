def go(index, sum):
    if index == N:
        c[sum] = True
        return
    go(index+1, sum+S[index])
    go(index+1, sum)

N = int(input())
S = list(map(int, input().split()))
c = [False] * (N*100000)
go(0, 0)
i = 1
while True:
    if not c[i]:
        break
    i += 1
print(i)