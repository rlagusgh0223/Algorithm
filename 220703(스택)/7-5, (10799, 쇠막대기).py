galho = list(input())
stack = []
cnt = 0
for i in range(len(galho)):
    if galho[i] == '(':
        stack.append(galho[i])
    elif galho[i] == ')' and galho[i-1] == '(':
        stack.pop()
        cnt += len(stack)
    elif galho[i] == ')':
        stack.pop()
        cnt += 1

print(cnt)