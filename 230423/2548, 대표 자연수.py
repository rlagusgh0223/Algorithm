import sys
N = int(sys.stdin.readline())
lst = list(map(int, sys.stdin.readline().split()))
lst.sort()
if N%2 == 0:
    print(lst[N//2-1])
else:
    print(lst[N//2])

# 이렇게 하면 시간초과 나온다
# 부르트포스가 왜 순서대로 계산하면 시간초과가 나오는지 모르겠지만 아무튼 중앙값을 구하는 문제란다...
# import sys
# N = int(sys.stdin.readline())
# lst = list(map(int, sys.stdin.readline().split()))
# ck, ans = 10001, 0  # 최소를 구하기 위한 합의 값, 대표 자연수
# for i in range(N):
#     now = 0
#     for j in range(N):
#         now += abs(lst[i]-lst[j])
#     if ck > now:
#         ck = now
#         ans = lst[i]
#     elif ck==now and ans>lst[i]:
#         ans = lst[i]
# print(ans)