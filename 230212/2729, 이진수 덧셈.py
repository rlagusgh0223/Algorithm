import sys
T = int(sys.stdin.readline())
for _ in range(T):
    a, b = sys.stdin.readline().split()
    a = int(a, 2)  # int함수 : (변환할 수, 진법)
    b = int(b, 2)
    print(bin(a+b)[2:])  # bin함수 : 정수를 0b가 붙은 이진 문자열로 변환