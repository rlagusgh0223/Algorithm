import sys
N = int(sys.stdin.readline())
check = list(map(int, sys.stdin.readline().split()))
ans = 0
cnt = 0
for now in check:
    if now == 1:
        cnt += 1
    else:
        cnt = 0
    ans += cnt
print(ans)

# 이게 왜 틀린건지 모르겠는데 틀렸다고 나온다
# import sys
# N = int(sys.stdin.readline())
# check = list(map(int, sys.stdin.readline().split()))
# ans = [0] * 10
# ans[0] = check[0]  # 첫번째 수는 0이 오든 1이 오든 그 값 그대로 더하면 된다
# for i in range(1, 10):
#     if check[i] == 1:
#         ans[i] = ans[i-1] + 1
# print(sum(ans))