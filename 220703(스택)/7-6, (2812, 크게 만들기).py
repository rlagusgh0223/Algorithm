import sys
N, K = map(int, sys.stdin.readline().split())
number = [word for word in sys.stdin.readline().rstrip()]
result = []
check = K

for i in range(N):
    while result and check>0 and result[-1]<number[i]:
        result.pop()
        check -= 1
    result.append(number[i])

print(''.join(result[:N-K]))