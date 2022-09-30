import sys
N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
stack = [0]
answer = [-1] * N
for num in range(N):
    while stack and A[stack[-1]] < A[num]:
        answer[stack[-1]] = A[num]
        stack.pop()

    stack.append(num)

for i in range(len(answer)-1):
    print(answer[i], end=' ')
print(answer[-1])




# 시간초과
# 오리지널 내 코드
# def NGE(num):
#     for chk in range(num+1, N):
#         if A[num] < A[chk]:
#             return A[chk]
#     return -1

# import sys
# N = int(sys.stdin.readline())
# A = list(map(int, sys.stdin.readline().split()))
# stack = []
# for num in range(N):
#     stack.append(NGE(num))
# for i in range(len(stack)-1):
#     print(stack[i], end=' ')
# print(stack[-1])