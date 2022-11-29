def go(index, sum):
    global ans
    if index == N:
        if sum == S:
            ans += 1
        return
    go(index+1, sum+a[index])
    go(index+1, sum)

N, S = map(int, input().split())
a = list(map(int, input().split()))
ans = 0
go(0, 0)
if S == 0:
    ans -= 1
print(ans)