# 접근은 맞았으나 파이썬의 round함수가 내가 생각한 결과가
# 우리가 생각하는거랑 다르게 나와서 틀렸다고 나온다고 한다
# math의 ceil()함수를 쓰면 맞았다고 나온다
import sys, math
num = list(sys.stdin.readline().rstrip())
ans = [0]*10
for i in num:
    ans[int(i)] += 1
ans[6] = ans[9] = math.ceil((ans[6]+ans[9]) / 2)
print(max(ans))