import sys
A, B, C = map(int, sys.stdin.readline().split())
# 순서는 바뀌지 않으므로 3개의 수를 곱하고 나누는건 두가지 경우밖에 없다
# 소수점 아래는 버린다고 했으므로 //가 아니라 /연산 후 int로 변환해줘야 한다
x = A*B / C
y = A / B*C
if x > y:
    print(int(x))
else:
    print(int(y))