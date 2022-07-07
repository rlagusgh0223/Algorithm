stack = list(input())
lst = []
cnt = 0

for now in range(len(stack)):
    if stack[now] == '(':
        lst.append('(')
    elif stack[now-1]=='(' and stack[now] == ')':
        lst.pop()
        cnt += len(lst)
    elif stack[now] == ')':
        lst.pop()
        cnt += 1

print(cnt)