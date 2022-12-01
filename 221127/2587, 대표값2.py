import sys
lst = []
for _ in range(5):
    lst.append(int(sys.stdin.readline()))
lst.sort()
print(sum(lst)//5)
print(lst[2])