galho = input()
stack = []
answer = 0
for i in range(len(galho)):
    if galho[i] == '(':    # '('를 만날때마다 스택에 '('를 추가한다
        stack.append(galho[i])
    else:    # ')'를 만나고
        if galho[i-1] == '(':    # stack의 최상단이 '('이면
            stack.pop()    # 이번 계산에 쓰인 '('는 빼준다. ')'는 stack에 입력을 한적이 없으니 뺄 필요 없다
            answer += len(stack)    # stack의 개수만큼 더한다
        else:    # (7번줄에 이어) stack의 최상단이 '('가 아니면
            stack.pop()
            answer += 1    # 총 개수에 1을 더해준다
print(answer)