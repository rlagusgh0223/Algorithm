import sys
input = sys.stdin.readline
N, M = map(int, input().split())
lst1 = [input().rstrip() for _ in range(N)]
lst2 = [input().rstrip() for _ in range(N)]
for i in range(N):
    compare = ''
    ck = True
    for j in lst1[i]:
        compare += j*2
    if compare != lst2[i]:
        ck = False
        break
print("Eyfa" if ck else "Not Eyfa")



# 시간과 메모리는 같지만 위의 코드가 더 간결해서 남겼다
# import sys
# N, M = map(int, sys.stdin.readline().split())
# lst1 = ['' for _ in range(N)]
# lst2 = ['' for _ in range(N)]
# for i in range(N):
#     lst1[i] = sys.stdin.readline().rstrip()
# for i in range(N):
#     lst2[i] = sys.stdin.readline().rstrip()

# for i in range(N):
#     for j in range(len(lst1[i])):
#         for k in range(j*2, j*2+2):
#             ck = False
#             if lst1[i][j] != lst2[i][k]:
#                 ck = True
#                 break
#         if ck:
#             break
#     if ck:
#         break
# if ck:
#     print("Not Eyfa")
# else:
#     print("Eyfa")