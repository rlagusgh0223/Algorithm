import sys
n = int(sys.stdin.readline())
for _ in range(n):
    N = int(sys.stdin.readline())
    cloth = {}
    answer = 1
    for _ in range(N):
        name, type = sys.stdin.readline().split()
        if type in cloth:
            cloth[type] += 1
        else:
            cloth[type] = 1
    for now in cloth:
        answer *= cloth[now]+1
    print(answer-1)