# 시간은 별 차이 없지만 메모리는 더 적게 쓰고 코드도 간편하다
import sys
n, d = map(int, sys.stdin.readline().split())
cnt = 0
for i in range(1, n+1):
    for now in str(i):
        if int(now) == d:
            cnt += 1
print(cnt)


# import sys
# n, d = map(int, sys.stdin.readline().split())
# lst = list(range(1,n+1))
# cnt = 0
# for i in range(n):
#     if lst[i]%10==d:
#         cnt += 1
#     while lst[i]//10 != 0:
#         lst[i] = lst[i]//10
#         if lst[i]%10 == d:
#             cnt += 1
# print(cnt)