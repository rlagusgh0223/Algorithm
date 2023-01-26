import sys
N, m, M, T, R = map(int, sys.stdin.readline().split())
now = m
cnt = ck = 0
while ck < N:
    if m+T > M:
        break
    elif now+T <= M:
        ck += 1
        now += T
    else:
        now = max(now-R, m)
    cnt += 1
print(cnt if ck==N else -1)


# 아래 코드가 내 코드지만 위의 코드가 더 보기 쉬워서 남긴다
# 시간은 내 코드가 조금 더 빠르고 메모리는 동일하다
# import sys
# N, m, M, T, R = map(int, sys.stdin.readline().split())
# now = m
# cnt = ck = 0
# if m+T>M:
#     print(-1)
#     exit()
# while ck<N:
#     if now+T <= M:
#         ck += 1
#         now += T
#     elif now-R >= m:
#         now -= R
#     else:
#         now = m
#     cnt += 1
# print(cnt)