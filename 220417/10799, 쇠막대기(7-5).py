import sys
stick = list(sys.stdin.readline().rstrip())
stack = []
cnt = 0
# for i in range(len(stick)):
#     if stick[i] == '(':    # 현재 받은게 (인 경우 스택에 추가
#         stack.append(stick[i])
#     else:    # 현재 받은게 ) 인 경우
#         if stick[i-1] == '(':    # 이전에 (를 받아()가 되면
#             stack.pop()    # 스택에서 이전거 지우고
#             cnt += len(stack)    # 지금까지 개수만큼 갯수 추가
#         else:    # )인 경우
#             stack.pop()    # 이전에 (한거 제거
#             cnt += 1    # 개수에 1개 추가

for i in range(len(stick)):
    if stick[i] == '(':
        stack.append(stick[i])
    elif stick[i-1] == '(' and stick[i] == ')':
        stack.pop()
        cnt += len(stack)
    elif stick[i] == ')':
        stack.pop()
        cnt += 1

print(cnt)