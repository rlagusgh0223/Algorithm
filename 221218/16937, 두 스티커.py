H, W = map(int, input().split())
N = int(input())
r = [0] * N
c = [0] * N
for i in range(N):
    r[i], c[i] = map(int, input().split())
ans = 0
for i in range(N):
    r1, c1 = r[i], c[i]
    for j in range(i+1, N):
        r2, c2 = r[j], c[j]
        for rot1 in range(2):
            for rot2 in range(2):
                if r1+r2<=H and max(c1, c2)<=W:
                    temp = r1*c1 + r2*c2
                    if ans < temp:
                        ans = temp
                if max(r1, r2)<=H and c1+c2<=W:
                    temp = r1*c1 + r2*c2
                    if ans < temp:
                        ans = temp
                r2, c2 = c2, r2
            r1, c1 = c1, r1
print(ans)