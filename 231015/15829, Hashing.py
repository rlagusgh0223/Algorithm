# 해시함수
# 알파벳마다 아래 수식에 넣어서 나온 모든 값을 더한다
#   알파벳순서(ex. a=1, b=2) * 31^i
# 해당 값을 1234567891로 나눈다
import sys
L = int(sys.stdin.readline())
alp = sys.stdin.readline().rstrip()
ans = 0
for i in range(L):
    ans += ((ord(alp[i])-96) * (31**i))
print(ans % 1234567891)