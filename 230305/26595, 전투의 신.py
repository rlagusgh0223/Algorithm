# 전투력이 최대이고 비용이 N 이하이면 되지
# 더 저렴한 비용을 찾으라는 내용은 문제에 없다
import sys
N = int(sys.stdin.readline())
A, PA, B, PB = map(int, sys.stdin.readline().split())
ck = a = b = 0
for i in range(N+1):
    cntA = (N-i)//PA
    cntB = i//PB
    now = A*cntA + B*cntB
    if ck < now:
        ck = now
        a = cntA
        b = cntB
print(a, b)