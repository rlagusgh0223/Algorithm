import sys, math

M = int(sys.stdin.readline())    # 시작값과 끝값 입력
N = int(sys.stdin.readline())
lst = []    # 범위 내에서 제곱수인 값 받는 리스트

for i in range(M, N+1):    # M부터 N까지
    x = math.sqrt(i)    # x는 해당 숫자의 제곱근
    # x = i ** (1/2)    # 파이썬에서 제곱근은 math함수에서 제공하지만, 세제곱근 부터는 제공하지 않으므로 이 방법으로 구해야 한다.
    if i // x == x and i % x == 0:    # 해당 숫자에서 제곱근으로 나눴을때 제곱근의 수가 나오고, 나머지가 없는 경우 즉, 제곱수인 경우
        lst.append(i)

if len(lst) == 0:    # 리스트가 비어있다면 -1 출력
    print("-1")
else:    # 리스트가 있다면 값들의 합과 최솟값 출력
    print(sum(lst))
    print(min(lst))