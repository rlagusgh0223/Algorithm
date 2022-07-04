stick = list(input())
galho = []
cnt = 0
for i in range(len(stick)):
    if stick[i] == '(':
        galho.append('(')
    elif stick[i] == ')' and stick[i-1] == '(':
        galho.pop()
        cnt += len(galho)
    elif stick[i] == ')':
        galho.pop()
        cnt += 1

print(cnt)