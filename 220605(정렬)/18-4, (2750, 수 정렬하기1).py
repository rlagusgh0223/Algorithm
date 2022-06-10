import sys
n = int(sys.stdin.readline())
lst = []
for i in range(n):
    lst.append(int(sys.stdin.readline()))

for i in range(n):
    for j in range(i+1, n):
        if lst[i] > lst[j]:
            lst[i], lst[j] = lst[j], lst[i]

for i in lst:
    print(i)