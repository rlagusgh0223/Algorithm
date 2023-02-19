# 0강부터 x강까지라는데 0으로 나눌 수 없으므로 1부터 시작해서 나눈다
# 최대확률을 내야되므로 확률 높은 순으로 9번 곱한다
# 상오차가 10^-6이므로 실수자리 6자리까지 허용한다
import sys
ans = 1
lst = [float(sys.stdin.readline()) for _ in range(10)]
lst.sort(reverse=True)
for i in range(9):
    ans *= lst[i]/(i+1)
print(round(ans*(10**9), 6))