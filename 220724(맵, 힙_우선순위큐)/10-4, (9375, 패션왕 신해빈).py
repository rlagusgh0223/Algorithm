import sys
n = int(sys.stdin.readline())
for _ in range(n):
    m = int(sys.stdin.readline())
    cloth = {}
    answer = 1
    for _ in range(m):
        Name, Type = sys.stdin.readline().split()
        if Type in cloth:
            cloth[Type] += 1
        else:
            cloth[Type] = 1
    for now in cloth:
        answer *= (cloth[now]+1)
    print(answer-1)