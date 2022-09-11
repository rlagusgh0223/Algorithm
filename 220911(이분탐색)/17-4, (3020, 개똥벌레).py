import sys

def upper(s, e, d, L):  # 숫자 초과값이 처음으로 나오는 인덱스 반환
    while e-s > 0:
        m = (s+e) // 2
        if L[m] <= d:
            s = m+1
        else:
            e = m
    return e

def lower(s, e, d, L):  # 숫자 이상의 값이 처음으로 나오는 인덱스 반환
    while e-s > 0:
        m = (s+e) // 2
        if L[m] < d:
            s = m+1
        else:
            e = m
    return e

up = []   # 장애물을 위->아래 상태로 저장하기 위한 배열
down = []  # 장애물을 아래->위 상태로 저장하기 위한 배열
result = [0] * 500001  # 후에 최솟값이 몇 개 있는지 파악하기 위해 쓰인다
n , h = map(int, sys.stdin.readline().split())
for i in range(n):
    obstacle = int(sys.stdin.readline())
    if i%2 == 1:  # 홀수는 up에, 짝수는 down에 넣는다
        up.append(obstacle)
    else:
        down.append(obstacle)

up.sort()
down.sort()

answer = 0  # 최솟값의 개수
mx = 2147483647  # 최솟값을 찾기 위한 값 초기화

for i in range(1, h+1):  # 높이 1부터 h까지 반복
    idxd = lower(0, len(down), i, down) # 아래->위 장애물을 처음 만나는 위치를 찾는다
    idxu = lower(0, len(up), h-i+1, up)  # 위->아래 장애물을 처음 만나는 위치를 찾는다
    result[i] = n//2-idxd + n//2-idxu
    mx = min(mx, result[i])

for i in range(1, h+1):
    if result[i] == mx:  # result배열에서 최솟값이 있다면 개수를 세어준다
        answer += 1

print(mx, answer)  # 최솟값과 최소값의 개수 출력