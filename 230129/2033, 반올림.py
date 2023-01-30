import sys
N = int(sys.stdin.readline())
d = 10
while N > d:
    if N%d >= d//2:
        N += d
    N -= N%d
    d *= 10
print(N)



# 이게 내 코드
# import sys
# N = [int(x) for x in sys.stdin.readline().rstrip()]
# for i in range(len(N)-1, 0, -1):
#     if N[i] >= 5:
#         N[i-1] += 1
#         N[i] = 0
#     else:
#         N[i] = 0
# print(*N, sep='')