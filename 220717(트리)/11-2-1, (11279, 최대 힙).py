import sys
import heapq    # 파이썬에서는 우선순위 큐 사용을 위해 heapq 라이브러리를 이용한다

n = int(input())
heap = []    # heap배열을 하나 만든다

for _ in range(n):
    num = int(sys.stdin.readline())    # 각각의 입력에 대하여
    if num != 0:    # 입력 데이터의 값이 자연수라면 우선순위 큐에 데이터 추가
        heapq.heappush(heap, -num)    # heapq 자체는 최소 힙을 기반으로 구현되어 있으므로 -num을 넣어줌으로써 가장 낮은 값을 힙의 루트에 위치해줬다heapq.heappush(배열, 데이터값)
    else:    # 입력 데이터의 값이 0이라면
        try:    # 배열이 비어있지 않다면
            print(-1 * heapq.heappop(heap))    # 가장 큰 값을 출력하고 우선순위 큐에서 삭제heapq.heappop(배열)
            # 최소 힙에서 최대 힙을 사용하기 위해 반전화해 둔 값을 다시 원상으로 복귀
        except:    # 배열이 비어 있는 경우 0을 출력
            print(0)