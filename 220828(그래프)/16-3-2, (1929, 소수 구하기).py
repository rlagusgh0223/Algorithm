def prime_check(num):  # 소수 판별을 위한 함수
    if num == 1:  # 1은 소수가 아니므로 False
        return False
    else:
        for i in range(2, int(num**0.5)+1):  # 2~해당수를 루트로 나눈 값의 정수값 까지의 수를 반복하여
            if num%i == 0:  # i로 나누어 떨어진다면 소수가 아니므로 False
                return False
        return True  # 나누어 떨어지지 않는다면 소수이므로 True

M, N = map(int, input().split())

for i in range(M, N+1):  # M ~ N의 수 탐색
    if prime_check(i):  # 해당 수가 소수라면 출력
        print(i)