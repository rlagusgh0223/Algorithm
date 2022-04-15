import sys
ans = list(map(int, sys.stdin.readline().rstrip()))
cnt = len(ans)//2
left = 0
right = 0
for i in range(len(ans)):
    if i < cnt:
        left += ans[i]
    else:
        right += ans[i]

if left == right:
    print("LUCKY")
else:
    print("READY")