import sys
lst = []
cnt = []
ans = 0
for i in range(8):
    lst.append([int(sys.stdin.readline()), i+1])
lst.sort()
for i in range(3, 8):
    ans += lst[i][0]
    cnt.append(lst[i][1])
cnt.sort()
print(ans)
print(*cnt, sep=' ')