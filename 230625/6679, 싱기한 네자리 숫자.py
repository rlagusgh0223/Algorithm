for now in range(1000, 10000):
    # 16진수
    num = now
    sixteen = 0
    while num != 0:
        sixteen += num % 16
        num //= 16

    # 12진수
    num = now
    twelve = 0
    while num != 0:
        twelve += num % 12
        num //= 12

    # 10진수
    num = now
    ten = 0
    while num != 0:
        ten += num % 10
        num //= 10

    if ten == sixteen == twelve:
        print(now)