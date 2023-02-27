# 아래 코드가 시간초과 나지만 맞았다고 가정하면
# import sys
# N = int(sys.stdin.readline())
# cnt = 0
# for i in range(10**(N-1), 10**N):
#     ck = True
#     for j in str(i):
#         j = int(j)
#         if j!=0 and j!=1 and j!=2:
#             ck = False
#             break
#     if ck and i%3==0:
#         cnt += 1
# print(cnt)

# 아래와 같이 결과가 나온다
# N=1 이면 0
# N=2 이면 2
# N=3 이면 6
# N=4 이면 18
# N=5 이면 54
# N=6 이면 162

# 점화식을 다음과 같이 도출할 수 있다.
# dp[i] = dp[i-1]*3



import sys
N = int(sys.stdin.readline())
dp = [0, 2]
for i in range(2, N):
    dp.append(dp[i-1]*3)
print(dp[N-1])