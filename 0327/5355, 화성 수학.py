import sys
n = int(sys.stdin.readline())
lst = []

for i in range(n):    # 앞에 소수도 받고 문자열로도 받는데 받는 길이도 다르면 리스트에 넣어서 각자의 경우에 맞춰 식을 운용하게 해야겠다고 생각하여 리스트에 입력하게 했다
    lst.append(list(map(str, sys.stdin.readline().split())))

for i in range(n):
    result = 0    # 어차피 j == 0 일때 초기화 되기는 하겠지만 그래도 새로 계산한다고 인식하기 위해서 0으로 설정해줬다.
    for j in range(len(lst[i])):    # j == 0일때 실수로 받기 위해 직접 주지 않고 길이에 맞춰서 주게 했다.
        if j == 0:    # 맨 앞의 값은 실수로 받는다
            result = float(lst[i][j])
        else:    # 그 밖의 입력은 문제에서 주어진 계산을 한다
            if lst[i][j] == '@':
                result *= 3
            elif lst[i][j] == '%':
                result += 5
            elif lst[i][j] == '#':
                result -= 7
    print("{:.2f}".format(result))    # 소수 둘째자리 까지 출력을 하므로 format을 이용한다