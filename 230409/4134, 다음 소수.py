# M이 소수이면 제곱근 M이 그보다 작거나 같은 수에 나누어 떨어지는 경우는 없다
def check(n):
    for i in range(2, int(n**0.5)+1):
        if n%i == 0:
            return False
    return True

import sys
for _ in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    while True:
        if n==0 or n==1:
            print(2)
            break
        elif check(n):
            print(n)
            break
        n += 1