import sys
N, K = map(int, sys.stdin.readline().split())
lst = [int(num) for num in sys.stdin.readline().rstrip()]
cnt = K
answer = []

for i in range(N):
    while answer and cnt>0 and int(answer[-1])<lst[i]:
        answer.pop()
        cnt -= 1
    answer.append(str(lst[i]))

print(''.join(answer[:N-K]))