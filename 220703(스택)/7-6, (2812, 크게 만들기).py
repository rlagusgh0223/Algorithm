import sys
N, K = map(int, sys.stdin.readline().split())
lst = [int(now) for now in sys.stdin.readline().rstrip()]
answer = []
cnt = K

for now in lst:
    while answer and cnt>0 and int(answer[-1])<now:
        answer.pop()
        cnt -= 1
    answer.append(str(now))

print(''.join(answer[:N-K]))