import sys
galho = [now for now in sys.stdin.readline().rstrip()]
answer = []
cnt = 0

for i in range(len(galho)):
    if galho[i] == '(':
        answer.append('(')
    elif galho[i]==')' and galho[i-1]=='(':
        answer.pop()
        cnt += len(answer)
    elif galho[i]==')':
        answer.pop()
        cnt += 1

print(cnt)