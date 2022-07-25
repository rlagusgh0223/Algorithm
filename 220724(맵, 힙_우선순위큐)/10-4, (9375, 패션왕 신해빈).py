n = int(input())
for _ in range(n):
    N = int(input())
    cloth = {}
    answer = 1
    for _ in range(N):
        name, Type = input().split()
        if Type in cloth:
            cloth[Type] += 1
        else:
            cloth[Type] = 1
    for now in cloth:
        answer *= cloth[now]+1
    print(answer - 1)