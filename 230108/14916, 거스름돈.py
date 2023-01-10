# dp를 이용한 방식
# 1 : -1
# 2 : 5x0 + 2x1
# 3 : -1
# 4 : 5x0 + 2x2
# ------------------
# 5 : 5x1 + 2x0
# 6 : 5x0 + 2x3
# 7 : 5x1 + 2x1
# 8 : 5x0 + 2x4
# 9 : 5x1 + 2x2
# ------------------
# 이후로는 2는 쭉 같은 패턴, 5는 이전패턴보다 1만 증가한다
# 동전 수를 세는 문제이므로 이전 패턴에서 1만큼만 더하면 된다
# 10 : 5x2 + 2x0
# 11 : 5x1 + 2x3
# 12 : 5x2 + 2x1
# 13 : 5x1 + 2x4
# 14 : 5x2 + 2x2
# ------------------
# 15 : 5x3 + 2x0
import sys
n = int(sys.stdin.readline())
coin = [0, -1, 1, -1, 2, 1, 3, 2, 4, 3]
for i in range(10, n+1):
    coin.append(coin[i-5]+1)
print(coin[n])


# 내가 푼 방식
# import sys
# n = int(sys.stdin.readline())
# cnt = 0
# while True:
#     if n == 0:
#         print(cnt)
#         break
#     elif n < 0:
#         print(-1)
#         break
#     elif n%5 == 0:
#         cnt += n//5
#         n %= 5
#     else:
#         cnt += 1
#         n -= 2