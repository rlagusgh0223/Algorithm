def LCM(a, b):  # 최소공배수를 구학 ㅣ위한 함수
    return (a*b) // GCD(a, b)  # a*b를 최대공약수로 나누어준 값 반환

def GCD(a, b):  # 최대공약수를 구하는 함수
    if b % a:
        return GCD(b % a, a)  # 어느 하나를 나누어서 나누어 떨어질때까지 나눈다
    else:
        return a

n = int(input())
for i in range(n):
    a, b = map(int, input().split())
    print(LCM(a, b))