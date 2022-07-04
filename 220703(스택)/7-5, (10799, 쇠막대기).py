import sys
galho = sys.stdin.readline().rstrip()
answer = []
cnt = 0

for now in range(len(galho)):
    if galho[now] == '(':
        answer.append(galho[now])
    elif galho[now-1] == '(' and galho[now] == ')':
        answer.pop()
        cnt += len(answer)
    elif galho[now] == ')':
        answer.pop()
        cnt += 1

print(cnt)