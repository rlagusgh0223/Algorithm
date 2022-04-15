import sys

while True:    # -1을 입력받을때까지 반복
    n = int(sys.stdin.readline())
    lst = []    # 약수를 모아둘 리스트인 lst 초기화
    if n == -1:
        break

    for i in range(1, n):    # 입력받은 수의 약수이므로 1부터 자기 자신 이전의 숫자까지 다 대조해본다
        if n%i == 0:    # 입력받은 수의 약수면 lst에 대입(1,2,3,4....로 나눈 수가 0이라는건 나누어떨어지므로 약수라는 의미)
            lst.append(i)

    if sum(lst) == n:    # 약수들의 합이 자기 자신일때 출력
        print(n, "=", end=' ')
        for j in range(len(lst)-1):    # 중간에 '+'가 들어있으므로 마지막 수는 따로 출력 
            print(lst[j], "+", end=' ')
        print(lst[-1])
    else:    # 약수들의 합이 자기 자신이 아니면 해당 문구 출력
        print(n,"is NOT perfect.")