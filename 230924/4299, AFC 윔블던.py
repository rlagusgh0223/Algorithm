import sys
x, y = map(int, sys.stdin.readline().split())
if x < y:
    print(-1)
else:
    if ((x+y)//2 + (x-y)//2)==x and ((x+y)//2 - (x-y)//2)==y:
        print((x+y)//2, (x-y)//2)
    else:
        print(-1)


# import sys
# x, y = map(int, sys.stdin.readline().split())
# for i in range(1000):
#     for j in range(1000):
#         if i+j==x and i-j==y:
#             print(i, j)
#             exit()
# print(-1)