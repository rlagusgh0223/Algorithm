# 모범답안
# 뭐라는건지 모르겠다. 식을 왜 이런식으로 푸는건지...
import sys
n = int(sys.stdin.readline())
lst = list(map(int, sys.stdin.readline().split()))    # 누적합을 이용하기 위한 배열 생성
sum = [0] * 200001
map = {}
answer = 0

map[0] = 1    # if sum[i] in map 부분에서 연속된 배열의 합이 0일때를 확인하기 위해 초기화
for i in range(n):
    sum[i] = lst[i]
    if i != 0:
        sum[i] += sum[i-1]
    if sum[i] in map:    # 누적합에 해당하는 key값이 map에 있다면
        answer += 1    #  정답의 개수를 1 더해준다
        map.clear()    # map을 초기화해준다
        map[sum[i-1]] = 1    # 다시 삽입해야 하는 연속된 배열의 합이 0일때를 확인하기 위해 설정
    map[sum[i]] = 1    # 누적합이 자료구조에 있음을 표시
    print(map, answer)
print(answer)