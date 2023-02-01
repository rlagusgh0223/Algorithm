# 숫자 하나하나에 대한 B진수 값을 구하는게 아니라 전체 수를 B진수 한 값을 구하는거다
import sys
T = int(sys.stdin.readline())
for _ in range(T):
    n = int(sys.stdin.readline())
    for i in range(2, 65):
        now = n
        lst = []
        ck = True
        while now != 0:
            lst.append(now%i)
            now //= i
        for j in range(len(lst)//2):
            if lst[j] != lst[-(j+1)]:
                ck = False
                break
        if ck:
            break
    if ck:
        print(1)
    else:
        print(0)