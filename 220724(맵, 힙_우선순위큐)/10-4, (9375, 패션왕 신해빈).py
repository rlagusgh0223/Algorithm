n = int(input())
for _ in range(n):
    N = int(input())
    cloth = {}
    answer = 1
    for _ in range(N):
        name, type = input().split()
        if type in cloth:
            cloth[type] += 1
        else:
            cloth[type] = 1
    for now in cloth.keys():
        answer *= (cloth[now]+1)
    print(answer-1)