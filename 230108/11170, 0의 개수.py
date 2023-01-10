# index는 리스트에서 최초의 해당 문자의 위치를 리턴하는 함수고,
# count가 리스트 안에서 해당 문자가 몇 개인지 계산해주는 함수다
import sys
T = int(sys.stdin.readline())
for i in range(T):
    N, M = map(int, sys.stdin.readline().split())
    cnt = 0
    for now in range(N, M+1):
        now = str(now)
        cnt += now.count('0')
    print(cnt)