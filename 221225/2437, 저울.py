N = int(input())
A = sorted(list(map(int, input().split())))
ans = 0  # 만들 수 있는 최저
for now in A:
    if now <= ans+1:
        ans += now
    else:
        break
print(ans+1)