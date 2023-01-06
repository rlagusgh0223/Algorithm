import sys
N = int(sys.stdin.readline())
s = []
ans = []
for i in range(N):
    s.append(list(sys.stdin.readline().rstrip()))

for j in range(len(s[0])):  # 문자열 중에서 문자 위치
    ok = True
    for i in range(N-1):  # 몇번째 문자열인지
        if s[i][j] != s[i+1][j]:
            ok = False
    if ok:
        ans.append(s[0][j])
    else:
        ans.append('?')

print(*ans, sep='')