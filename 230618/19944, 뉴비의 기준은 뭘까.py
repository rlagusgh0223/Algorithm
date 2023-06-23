# 문제가 이해하기 어렵게 나왔다
# 1, 2 학년은 뉴비
# 뉴비보다 높은 학년이지만 N학년 이하면 올드비
# 뉴비도 아니고 N학년보다 높으면 TLE

import sys

N, M = map(int, sys.stdin.readline().split())
if M <= 2:
    print("NEWBIE!")
elif M <= N:  # 위의 조건문 때문에 어차피 M은 무조건 2보다 크다
    print("OLDBIE!")
else:  # M이 N보다 큰 경우
    print("TLE!")