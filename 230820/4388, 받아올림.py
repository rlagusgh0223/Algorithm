import sys
while True:
    x, y = sys.stdin.readline().split()
    if x=='0' and y=='0':
        break
    # x와 y의 자릿수 맞추기
    if len(x) > len(y):
        y = (len(x) - len(y))*'0' + y
    else:
        x = (len(y) - len(x))*'0' + x
    cnt = carry = 0
    for i in range(len(x)-1, -1, -1):
        if int(x[i]) + int(y[i]) + carry >= 10:
            cnt += 1
            carry = 1
        else:
            carry = 0
    print(cnt)