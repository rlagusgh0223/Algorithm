# 골드바흐의 추측은 10**18 = 1000000(백만) 이하에서는 맞다는게 증명됐다
import sys
MAX = 1000000
check = [True for _ in range(MAX+1)]
check[0] = check[1] = False
lst = []
for i in range(2, MAX+1):
    if check[i]:
        lst.append(i)
        j = i+i
        while j <= MAX:
            check[j] = False
            j += i

lst = lst[1:]  # 소수 리스트에서 2 제거
while True:
    n = int(sys.stdin.readline())
    if n==0:
        break
    for now in lst:
        if check[n-now]:
            print("{0} = {1} + {2}".format(n, now, n-now))
            break