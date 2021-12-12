n = int(input())
stk = [0] * n
for i in range(n):
    word = list(input())
    stk[i] = []
    for j in word:
        if j == '(':
            stk[i].append('(')
        elif j == ')':
            if len(stk[i]) == 0:
                stk[i].append(')')
                break
            else:
                stk[i].pop()

for i in range(n):
    if len(stk[i]) == 0:
        print("YES")
    else:
        print("NO")