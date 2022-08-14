N, M = map(int, input().split())
answer = []

def back(depth):
    if depth==M:
        print(' '.join(map(str, answer)))
        return
    for i in range(1, N+1):
        answer.append(i)
        back(depth+1)
        answer.pop()

back(0)