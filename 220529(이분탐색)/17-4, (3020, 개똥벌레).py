def upper_bound(s, e, d, L):    # 숫자 초과값이 처음으로 나오는 인덱스값 반환
    while e-s > 0:
        m = (s+e)//2
        if L[m] <= d:
            s = m+1
        else:
            e = m
    return e

def lower_bound(s, e, d, L):    # 숫자 이상의 값이 처음으로 나오는 인덱스값 반환
    while e-s > 0:
        m = (s+e)//2
        if L[m] < d:    # 이 부분 말곤 upper과 뭐가 다른지 모르겠다
            s = m+1
        else:
            e = m
    return e

up = []    # 장애물을 위 -> 아래 상태로 저장하기 위한 배열
down = []    # 장애물을 아래 -> 위 상태로 저장하기 위한 배열
result = []    # 장애물을 통과하는 수를 저장하기 위한 배열
n, h = map(int, input().split())
for i in range(n):
    obstacle = int(input())    # 홀수번째 장애물을 up배열에, 짝수번째 장애물은 down배열에 넣는다
    if i%2 == 1:
        up.append(obstacle)
    else:
        down.append(obstacle)

up.sort()
down.sort()

answer = 0    # 최솟값의 개수를 저장하기 위한 변수
mx = 214783647    # 최솟값을 찾는데 사용할 값

for i in range(1, h+1):
    idxd = lower_bound(0, len(down), i, down)
    idxu = lower_bound(0, len(up), h-i+1, up)
    now = n//2-idxd + n//2-idxu    # 장애물을 만나는 총 개수
    result.append(now)
    mx = min(mx, now)

for ans in result:
    if ans == mx:
        answer += 1

print(mx, answer)    # 최솟값과 최솟값의 개수 출력