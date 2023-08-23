import sys
grade = [100, 100, 200, 200, 300, 300, 400, 400, 500]
lst = list(map(int, sys.stdin.readline().split()))
for i in range(9):
    if lst[i] > grade[i]:
        print("hacker")
        exit()
if sum(lst) < 100:
    print("none")
else:
    print("draw")