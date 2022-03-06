import sys

def stars(n):
    arr = []    # 일차원 리스트 형태로 별의 모양을 받을 리스트
    for i in range(3 * len(n)):    # 여기서 n은 별 모양 리스트니까 len으로 바꿔서 만들어준다
        if i // len(n) == 1:    # 가운데 들어가는 부분은 공백
            print("\n",i, len(n), i%len(n))
            arr.append(n[i%len(n)] + " "*len(n) + n[i % len(n)])
        else:
            print(i, len(n), i%len(n))
            arr.append(n[i % len(n)] * 3)
    return arr

star = ["***", "* *", "***"]   # 가장 작은 형태 기본 모양
n = int(sys.stdin.readline())
k = 0
while n != 3:    # 가장 작은 형태 기본 모양을 기준으로 몇 번 가운데 공백 문양을 만들어야 하는지 계산
    n = n//3    # ex. 27을 입력하면 기본 모양을 기준으로 2번 더 가운데 빈 공간을 만드는 재귀함수 사용
    k += 1

for i in range(k):    # 위에서 만든 별 리스트를 star에 넘겨주고 출력
    star = stars(star)
for i in star:    # 일차원 리스트로 받은 별 모양을 값 별로 출력하여 문제에서 나온 모양대로 만듬
    print(i)