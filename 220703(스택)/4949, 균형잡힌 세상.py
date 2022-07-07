# answer= []
while True:
    word = list(input())
    stack = []
    check = 0

    if word[0] == '.':
        break
    for now in word:
        if now == '(':
            check += 1
            stack.append('(')
        elif now == '[':
            check += 1
            stack.append('[')
        
        elif now == ')':
            if len(stack) > 0 and stack[-1] == '(':
                check -= 1
                stack.pop()
            else:
                check -= 1
                break
        elif now==']':
            if len(stack) > 0 and stack[-1] == '[':
                check -= 1
                stack.pop()
            else:
                check -= 1
                break
        # print("stack", stack)

    if check != 0 or len(stack) != 0:
        print("no")
        # answer.append("no")
    else:
        print("yes")
#         answer.append("yes")
# print(answer)