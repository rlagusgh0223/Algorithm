# math함수 사용
import sys, math
L = int(sys.stdin.readline())
A = int(sys.stdin.readline())
B = int(sys.stdin.readline())
C = int(sys.stdin.readline())
D = int(sys.stdin.readline())
print(L - max(math.ceil(A/C), math.ceil(B/D)))



# import sys
# L = int(sys.stdin.readline())
# A = int(sys.stdin.readline())
# B = int(sys.stdin.readline())
# C = int(sys.stdin.readline())
# D = int(sys.stdin.readline())
# if A%C != 0:
#     a = A//C + 1
# else:
#     a = A//C
# if B%D != 0:
#     b = B//D + 1
# else:
#     b = B//D
# print(L - max(a, b))