N = int(input())
S = list(input())
cnt = 0
ans = 0
for now in range(len(S)):
    if S[now] == 'X':
        cnt = 0
    else:
        ans += (now+1) + cnt
        cnt += 1
print(ans)