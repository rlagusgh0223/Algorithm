# LRU : 가장 오래된 참조되지 않은 값을 지운다
def solution(cacheSize, cities):
    answer = 0
    q = deque()
    if cacheSize == 0:
        return len(cities) * 5
    for city in cities:
        city = city.lower()
        if city in q:
            answer += 1
            q.remove(city)
        else:
            answer += 5
            if len(q) >= cacheSize:
                q.popleft()
        q.append(city)
    return answer



from collections import deque
import sys
n = int(sys.stdin.readline())
city = list(sys.stdin.readline().split())
print(solution(n, city))