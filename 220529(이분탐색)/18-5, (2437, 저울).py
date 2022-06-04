n = int(input())
weight = list(map(int, input().split()))
weight.sort()

answer = 1    # 정답으로 나올 수 있는 최솟값 1로 변수를 초기화 한다
for i in weight:
    if answer<i:    # 저울추의 무게가 answer 변숫값보다 크다면 종료한다
        break
    answer += i    # 저울추의 무게가 answer 변숫값보다 작다면 answer변수에 저울추의 무게만큼 더해준다

print(answer)