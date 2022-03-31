import sys
A, B, C = map(int, sys.stdin.readline().split())
D = int(sys.stdin.readline())

# 아래 코드도 맞기는 한데 좀 비효율적인거 같아서 모범답안 추가한다
# while True:
#     if D == 0:
#         break
#     D -= 1
#     C += 1
#     if C == 60:
#         C = 0
#         B += 1
#     if B == 60:
#         B = 0
#         A += 1
#     if A == 24:
#         A = 0
#         B = 0
#         C = 0
# print(A, B, C)

#==================================

# 모범답안

# C1은 최종 초, B1은 60초 넘어서 분으로 넘어가는 값
C1 = (C+D) % 60
B1 = (C+D) // 60

# B2는 최종 분, A1은 60분 넘어서 시로 넘어가는 값
B2 = (B+B1) % 60
A1 = (B+B1) // 60

# 최종 시간 24로 나눈 값
A2 = (A+A1) % 24

print(A2, B2, C1)