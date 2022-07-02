n, k = map(int, input().split())
number = list(input())

answer = []
cnt = k
for num in number:
    # answer 스택이 비어있지 않고 지울 수 있는 횟수 k가 남아있고,
    # answer의 마지막 값이 num보다 작다면 answer의 마지막 값을 지운다
    while answer and cnt>0 and answer[-1]<num:
        del answer[-1]
        cnt -= 1
    answer.append(num)

print(''.join(answer[:n-k]))