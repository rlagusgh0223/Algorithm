N, K = map(int, input().split())
number = list(input())
cnt = K
answer = []

for num in number:
    while answer and cnt>0 and answer[-1]<num:
        answer.pop()
        cnt -= 1
    answer.append(num)

print(''.join(answer[:N-K]))