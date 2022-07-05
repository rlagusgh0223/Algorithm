# 틀렸다는데 뭐가 틀린건지 모르겠다
while True:
    word = list(input())
    stack = []
    check = 0
    if word[0] == '.':
        break
    for now in word:
        if now == '(':
            stack.append('(')
        elif now == '[':
            stack.append('[')
        elif now == ')':
            if len(stack)==0 or stack[-1]!='(':
                print("no")
                check = 1
                break
            elif stack[-1]=='(':
                stack.pop()
        elif now == ']':
            if len(stack)==0 or stack[-1]!='[':
                print("no")
                check = 1
                break
            elif stack[-1]=='[':
                stack.pop()
    if check==0:
        print("yes")