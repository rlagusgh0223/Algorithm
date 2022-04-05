import sys

while True:
    n, m = map(int, sys.stdin.readline().split())
    if n == 0 and m == 0:    # 0 0 을 입력하면 종료
        break
    if n/m > 0 and n%m == 0:    # 첫번째 수가 두번째 수의 배수인 경우
        print("multiple")
    elif m/n > 0 and m%n == 0:    # 첫번째 수가 두번째 수의 약수인 경우
        print("factor")
    else:    # 둘 다 아닌 경우
        print("neither")