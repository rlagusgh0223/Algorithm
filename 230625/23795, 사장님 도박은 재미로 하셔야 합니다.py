import sys
ans = 0
for i in range(2000):  # 이런건 while문이 맞지만, 문제에서 2000개 미만이라고 명시했으므로 for문으로 작성했다
    n = int(sys.stdin.readline())
    if n == -1:
        break
    ans += n
print(ans)