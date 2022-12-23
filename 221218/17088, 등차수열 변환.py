N = int(input())
B = list(map(int, input().split()))
if N == 1:
    print(0)
    exit()
ans = -1
for d1 in range(-1, 2):
    for d2 in range(-1, 2):
        change = 0
        if d1 != 0:
            change += 1
        if d2 != 0:
            change += 1
        ok = True
        a0 = B[0] + d1
        diff = (B[1]+d2) - a0
        an = a0 + diff
        for i in range(2, N):
            an += diff
            if B[i] == an:
                continue
            if B[i]-1==an or B[i]+1==an:
                change += 1
            else:
                ok = False
                break
        if ok:
            if ans==-1 or ans>change:
                ans = change
print(ans)