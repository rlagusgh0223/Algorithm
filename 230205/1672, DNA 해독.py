import sys
N = int(sys.stdin.readline())
A = list(sys.stdin.readline().rstrip())
lst = {"AG":"C", "AC":"A", "AT":"G", "GC":"T", "GT":"A", "CT":"G", "GA":"C", "CA":"A", "TA":"G", "CG":"T", "TG":"A","TC":"G"}
for _ in range(N-1):
    a, b = A[-2], A[-1]
    if a == b:
        del A[-1]
    ab = a+b
    if ab in lst:
        A[-2] = lst[ab]
        del A[-1]
print(*A)



# import sys
# N = int(sys.stdin.readline())
# A = list(sys.stdin.readline().rstrip())
# for _ in range(N-1):
#     lst = list(set([A[-1], A[-2]]))
#     if len(lst) == 1:
#         A[-2] = lst[0]
#         del A[-1]
#     elif 'A' in lst and 'G' in lst:
#         A[-2] = 'C'
#         del A[-1]
#     elif 'A' in lst and 'C' in lst:
#         A[-2] = 'A'
#         del A[-1]
#     elif 'A' in lst and 'T' in lst:
#         A[-2] = 'G'
#         del A[-1]
#     elif 'G' in lst and 'C' in lst:
#         A[-2] = 'T'
#         del A[-1]
#     elif 'G' in lst and 'T' in lst:
#         A[-2] = 'A'
#         del A[-1]
#     elif 'C' in lst and 'T' in lst:
#         A[-2] = 'G'
#         del A[-1]
# print(*A)