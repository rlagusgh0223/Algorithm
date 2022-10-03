import sys
N, M = map(int, sys.stdin.readline().split())
heard = []
see = []

for i in range(N):
    heard.append(sys.stdin.readline().rstrip())
for i in range(M):
    see.append(sys.stdin.readline().rstrip())

answer = list(set(heard) & set(see))
answer.sort()
print(len(answer))
for now in answer:
    print(now)