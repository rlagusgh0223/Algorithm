# 666, 1666, 2666, 3666, 4666, 5666, 6660, 6661
# 이 순서로 나와야 되기 때문에 666을 기준으로 숫자를 계산해야 된다

import sys
n = int(sys.stdin.readline())
x = 665

# 풀이 1
while n > 0:   # n = 0 일 때까지 반복
    x += 1
    if '666' in str(x):     # x에 '666'이 있을때마다 n을 감소시켜 666이 들어간 몇번째 수인지 구한다
        n -= 1
print(x)

# 풀이 2
# cnt = 0
# while True:
#     if '666' in str(x):     # x에 '666'이 들어가면 cnt를 1 증가시켜 몇번째 666인지 표시한다
#         cnt += 1
#     if cnt == n:
#         print(x)
#         break
#     x += 1
#     print("cnt:{0}, n:{1}, x:{2}".format(cnt, n, x))