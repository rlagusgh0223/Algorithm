import heapq    # 우선순위 큐 사용을 위해 heapq모듈을 import한다
N = int(input())    # N개의 카드를 입력받는다

card = list(int(input()) for _ in range(N))
heapq.heapify(card)    # n개의 카드를 힙으로 변환한다
answer = 0

while len(card) != 1:    # n이 1이라면 answer=0이 되므로 카드의 개수가 1이 아닐때까지 반복문을 돌린다
    first = heapq.heappop(card)    # 우선순위 큐에서 가장 작은 값 2개를 꺼낸다
    second = heapq.heappop(card)
    sum = first + second    # 합친 값을 answer에 더해준다
    answer += sum
    heapq.heappush(card, sum)    # 합친값을 우선순위 큐에 다시 넣어준다

print(answer)    # 정답을 출력한다