import sys
n = int(sys.stdin.readline())
client = list(map(int, sys.stdin.readline().split()))
check = list(map(int, sys.stdin.readline().split()))
cnt = 0
for now in client:
    now -= check[0]
    cnt += 1
    if now <= 0:
        continue
    if (now % check[1] == 0):
        cnt += now//check[1]
    elif now > 0:
        cnt += now//check[1] + 1
print(cnt)