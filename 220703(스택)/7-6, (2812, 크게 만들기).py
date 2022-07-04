import sys
N, K = map(int, sys.stdin.readline().split())
number = [now for now in sys.stdin.readline().rstrip()]
result = []
count = K

for num in number:
    while result and count>0 and result[-1]<num:
        result.pop()
        count -= 1
    result.append(num)

print(''.join(result[:N-K]))