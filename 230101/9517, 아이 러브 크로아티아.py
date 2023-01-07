import sys
input = sys.stdin.readline
K = int(input())
n = int(input())
lst = [input().split() for _ in range(n)]
ck = 0
for i in range(n):
    ck += int(lst[i][0])
    if ck>=210:
        break
    if lst[i][1]=='T':
        K = (K+1)%9
        if K == 0:
            K = 1
print(K)


# import sys
# input = sys.stdin.readline
# K = int(input())
# n = int(input())
# ck = 0
# for i in range(n):
#     T, Z = input().split()
#     ck += int(T)
#     if ck<210 and Z == 'T':
#         K += 1
#         if K == 9:
#             K = 1
# print(K)