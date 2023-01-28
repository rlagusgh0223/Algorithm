# 도저히 답이 안나와서 인터넷 참고했다
# 문제에서 주어진 함수를 이용하면 재귀함수 때문에 풀 수 없다
# 심지어 이마저도 pypy3로 풀어야 한다...
import sys
n = int(sys.stdin.readline())
f1, f2 = 0, 0
ans = n - 2  # 2번재 코드는 다이나믹 프로그래밍으로 처음 입력해야되는 1,2번째를 제외하고 n번째 까지 계산한다
x, y = 1, 1
for _ in range(n-2):
    y, x = (x+y)%1000000007, y
print(y, ans)