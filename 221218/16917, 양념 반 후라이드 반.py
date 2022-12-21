import sys
A, B, C, X, Y = map(int, sys.stdin.readline().split())
ans = A*X + B*Y
for i in range(1, 100001):
    price = 2*C*i + max(0, X-i)*A + max(0, Y-i)*B
    if ans > price:
        ans = price
print(ans)