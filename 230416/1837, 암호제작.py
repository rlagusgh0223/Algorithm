# 소수를 구한 다음에 풀면 시간초과 나온다
# 그냥 P에 K보다 작은 소인수가 있는지 확인만 하면 되므로 2부터 K까지 나누면 된다
import sys
P, K = map(int, sys.stdin.readline().split())
for i in range(2, K):
    if P%i == 0:
        print("BAD", i)
        exit()
print("GOOD")



# 되긴 하는데 시간이 오래 걸린다
# def ck(n):
#     for i in range(2, int(n**0.5)+1):
#         if n%i==0:
#             return False
#     return True

# import sys
# P, K = map(int, sys.stdin.readline().split())
# ans = []
# for i in range(2, K):
#     if ck(i):
#         ans.append(i)
# for now in ans:
#     if P%now == 0:
#         print("BAD", now)
#         exit()
# print("GOOD")