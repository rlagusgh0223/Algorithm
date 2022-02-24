# 지속적인 공부 필요
from math import sqrt
import sys
result = []

def sosu(a, b):
    cnt = 0
    check = [True] * (b+1)    # 우선 체크를 위해 2배까지 길이의 리스트 작성

    for i in range(2, int(sqrt(b) + 1)):    # 전부다 하면 시간초과. 소수는 2부터니까 2에서 시작하고, 제곱하면 2배(b)가 되는 수 까지만 구하면 소수인지 알 수 있다
        if check[i] == True:    # 2부터 확인점까지 
            for j in range(i*2, b+1, i):    # 이미 나온 수 의 배수는 소수가 아니므로 False를 줘서 카운트 하지 않게 한다
                check[j] = False
    
    for i in range(a+1, b+1):    # a부터 b까지(a는 포함시키지 않고 b는 포함시키기 위해 a+1, b+1)
        if check[i] == True:    # 위의 반복문에서 약수가 있는 수는 False를 만들어 줬다. 즉, 지금 True인건 소수
            cnt += 1    # cnt 1 증가
    return cnt    # cnt 결과값 리턴

while True:
    n = int(sys.stdin.readline())
    if n == 0:    # 0 입력하면 종료
        break
    result.append(sosu(n, 2*n))    # 소수 확인 범위는 그 숫자부터 2배까지

for i in result:    # 지금까지 입력한 각 숫자와 그 2배 사이의 소수 개수 출력
    print(i)