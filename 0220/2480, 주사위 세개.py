import sys
a, b, c = map(int, sys.stdin.readline().split())

if a == b == c:             # 세 수가 모드 같은 경우
    result = 10000 + a * 1000
elif a == b and b != c:     # 두 수만 같은 경우
    result = 1000 + a * 100
elif a == c and b != c:
    result = 1000 + a * 100
elif b == c and a != c:
    result = 1000 + b * 100
else:                       # 세 수 모두 다른 경우
    n = max(a,b,c)          # 세 수 중 가장 큰 값 찾기
    result = n * 100

print(result)