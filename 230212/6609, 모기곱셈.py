# 5개의 번데기가 있고 3번째가 살아남는다면, 1마리의 모기가 남게 된다.
# 6개의 번데기 중에서는 두마리의 성충 모기가 나올 것이다
# -> 살아남는 번데기 중 3번째 번데기가 살아남는다면 3, 6, 9 ~ 이런식으로 갈 텐데
#    5개의 번데기면 3번만, 6개의 번데기면 3, 6번이 살아남는다는 것 같다
import sys
while True:
    try:
        M, P, L, E, R, S, N = map(int, sys.stdin.readline().split())
        for i in range(N):
            M, P, L = P//S, L//R, M*E
        print(M)
    except:
        break