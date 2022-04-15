import sys
n = int(sys.stdin.readline())
A = 300
B = 60
C = 10

# 덧셈을 최소화해야 되므로 큰 수부터 나눠서 남은 값을 다음 값이 받아서 나누는 식으로 한다
a1 = n // A
a2 = n % A

b1 = a2 // B
b2 = a2 % B

c1 = b2 // C
c2 = b2 % C

if c2 != 0:
    print("-1")
else:
    print(a1, b1, c1)