import sys
lst = list(map(int, sys.stdin.readline().split()))
lst.sort()
d = min(lst[1] - lst[0], lst[2] - lst[1])
for i in range(3):
    temp = lst[i]
    if temp+d not in lst:
        print(temp + d)
        break