# import sys
# A, B, C, N = map(int, sys.stdin.readline().split())
# x, y, z = 0, 0, 0
# while A*x+B*y+C*z <= N:
#     while A*x+B*y+C*z <= N:
#         while A*x+B*y+C*z <= N:
#             if A*x + B*y + C*z == N:
#                 print(1)
#                 exit()
#             z += 1
#         z = 0
#         y += 1
#     y = 0
#     x += 1
# print(0)

# 원리는 같지만 for문으로 간단하게 할 수 있다
# 조건이 충족되면 반복문을 정지하기 위해 함수로 만들었다
def check(A, B, C, N):
    for i in range(N//A+1):
        for j in range(N//B+1):
            for k in range(N//C+1):
                if A*i + B*j + C*k == N:
                    return 1
    return 0

import sys
A, B, C, N = map(int, sys.stdin.readline().split())
print(check(A, B, C, N))