import sys
lst = list(sys.stdin.readline().rstrip())
stack = []
cnt = 0

for now in range(len(lst)):
    if lst[now] == '(':
        stack.append('(')
    elif lst[now-1] == '(' and lst[now] == ')':
        stack.pop()
        cnt += len(stack)
    elif lst[now] == ')':
        stack.pop()
        cnt += 1

print(cnt)