import sys
N = int(sys.stdin.readline())
print("int a;")
print("int *ptr = &a;")
if N >= 2:
    print("int **ptr2 = &ptr;")
for i in range(3, N+1):
    print("int {}ptr{} = &ptr{};".format('*'*i, i, i-1))