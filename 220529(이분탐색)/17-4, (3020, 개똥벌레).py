def upper_bound(s, e, d, L):    # 숫자 초과값이 처음으로 나오는 인덱스 반환
    while e-s > 0:
        m = (s+e) // 2
        if L[m] <= d:
            s = m + 1
        else:
            e = m
    return e

def lower_bound(s, e, d, L):    # 숫자 이상의 값이 처음으로 나오는 인덱스 반환
    while e-s > 0:
        m = (s+e) // 2
        if L[m] < d:    # 여기 < 빼고는 upper_bound와 똑같다
            s = m + 1
        else:
            e = m
    return e

up = []    # 동굴의 장애물을 위 -> 아래 상태로 저장하기 위한 배열
down = []    # 아래 -> 위 상태로 저장하기 위한 배열
#result = [0]*500001    # 장애물을 통과하는 수를 저장해두기 위한 result의 크기를 높이 h로 해두었다. 최솟값이 몇 개 있는지 파악하기 위해 쓰인다
result = [0]
n, h = map(int, input().split())
for i in range(n):
    obstacle = int(input())
    if i%2 == 1:    # 홀수번째 장애물은 up에, 짝수번째 장애물은 down에 입력
        up.append(obstacle)
    else:
        down.append(obstacle)

up.sort()
down.sort()

answer = 0    # 최솟값의 개수를 저장하기 위한 변수
mx = 2147483647    # 최솟값을 찾기 위한 값

for i in range(1, h+1):    # 높이 1부터 h까지 반복
    idxd = lower_bound(0, len(down), i, down)    # 아래 -> 위 장애물을 처음 만나는 위치를 찾는다
    idxu = lower_bound(0, len(up), h-i+1, up)    # 위 -> 아래 장애물을 처음 만나는 위치를 찾는다
    #result[i] = n//2-idxd + n//2-idxu    # 장애물을 만나는 총 개수는 n/2-idxd + n/2-idxu와 같다
    result.append(n//2-idxd + n//2-idxu)
    mx = min(mx, result[i])    # 장애물을 만나는 총 개수 중 최솟값을 찾는다

for i in range(1, h+1):    # result배열을 순회하면 최솟값의 개수를 센다
    if result[i] == mx:
        answer += 1

print(mx, answer)    # 최솟값과 최솟값의 개수 출력