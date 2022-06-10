import sys
n = int(sys.stdin.readline())
member = []
for i in range(n):
    x, y = sys.stdin.readline().split()
    member.append([int(x), y])

member.sort(key=lambda x:x[0])

for i in member:
    print(i[0], i[1])