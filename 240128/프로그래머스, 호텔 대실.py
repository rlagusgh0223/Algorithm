from heapq import heappush, heappop
def solution(book_time):
    answer = 0
    book_time = [[int(s[:2])*60 + int(s[3:]), int(e[:2])*60 + int(e[3:]) + 10] for s, e in book_time]
    book_time.sort()
    heap = []
    for book in book_time:
        # heap[0]에는 언제나 가장 작은 값이 온다
        if heap and heap[0]<=book[0]:
            # heappop()은 heap에서 가장 작은 값을 지운다
            heappop(heap)
        else:
            answer += 1
        heappush(heap, book[1])
    return answer

import sys
book = list(sys.stdin.readline().strip().split('"], ["'))
book = list(b.split('", "') for b in book)
print(solution(book))