# 시간초과
# import sys
# N = int(sys.stdin.readline())
# heap = []
# for i in range(N):
#     x = int(sys.stdin.readline())
#     if x == 0:    # 입력된 수가 0이고
#         if not heap:    # 배열에 아무 수도 없다면
#             print('0')    # 0 출력하고 이번 순서 종료해서 에러 안뜨게 한다
#             continue
#         MAX = heap[0]    # 수가 입력될때마다 현재 힙에서 가장 큰 값을 MAX에 넣기 위해 제일 처음 값으로 초기화한다
#         cnt = 0    # heap에서 가장 큰 값의 위치를 나타낼 변수, 배열에 값이 1개뿐이라 반복문이 돌아가지 않을경우 처음 값을 지우기 위해 여기서 초기화
#         for j in range(len(heap)):    # 현재 배열의 길이만큼
#             if MAX < heap[j]:    # 더 큰값이 있는지 확인
#                 MAX = heap[j]
#                 cnt = j
#         del heap[cnt]    # 현재 최대값 삭제
#         print(MAX)    # 삭제된 최대값 출력
#     else:
#         heap.append(x)    # 입력값 배열에 추가


##########################################
# 모범답안
# import sys
# import heapq
# n = int(sys.stdin.readline())
# heap = []

# for _ in range(n):
#     num = int(sys.stdin.readline())
#     if num != 0:
#         heapq.heappush(heap, -num)    # 데이터 삽입 : heapq.heappush(배열, 데이터값) heapq 자체는 최소힙을 기반으로 구현되어 있으므로 -num을 넣어줘 가장 낮은 값을 힙의 루트에 위치
#     else:
#         try:
#             print(-1 * heapq.heappop(heap))    # 우선순위가 가장 높은 데이터 삭제 : heapq.heappop(배열)
#         except:
#             print(0)

###########################################

import sys
import heapq
N = int(sys.stdin.readline())
heap = []
for i in range(N):
    x = int(sys.stdin.readline())
    if x == 0:    # 입력된 수가 0이고
        if not heap:    # 배열에 아무 수도 없다면
            print('0')    # 0 출력하고 이번 순서 종료해서 에러 안뜨게 한다
            continue
        print(heapq.heappop(heap) * -1)
    else:
        heapq.heappush(heap, -x)    # 입력값 배열에 추가