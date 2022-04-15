import sys
n = int(sys.stdin.readline())    # 라운드 입력
Cang = Sang = 100    # Cang는 창영이점수, Sang는 상덕이 점수

for i in range(n):    # 입력한 수 만큼 반복
    x, y = map(int, sys.stdin.readline().split())    # 띄어쓰기를 기준으로 구분하여 두 사람의 점수 입력
    # 주사위가 낮은 사람은 높은 사람의 점수만큼 점수가 깎인다. 주사위가 같으면 아무일도 일어나지 않는다.
    if x > y:
        Sang -= x
    elif x < y:
        Cang -= y

print(Cang)
print(Sang)