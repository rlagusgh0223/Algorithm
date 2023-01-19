import sys
N = list(map(int, list(sys.stdin.readline().rstrip())))
for i in range(1, len(N)):
    left, right = 1, 1
    for j in range(i):
        left *= N[j]
    for j in range(i, len(N)):
        right *= N[j]
    if left == right:
        print("YES")
        exit()
print("NO")