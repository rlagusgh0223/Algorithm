import sys

def factorial(x):
    if x>1:    # 받은 값이 1보다 크다면
        y = factorial(x-1)    # 받은 값에서 1을 빼고 재귀함수로 자기자신 호출
    else:    # 받은 값이 1 이하이면
        return 1   # 1 리턴
    return x * y    # 받은 값이 1보다 크면 팩토리얼 함수로부터 받은 값(이전까지 수 들의 곱)과 지금 내 값을 곱해서 리턴

N = int(sys.stdin.readline())    # 입력한 값 받는 변수
print(factorial(N))    # 함수를 이용한 팩토리얼 결과 출력