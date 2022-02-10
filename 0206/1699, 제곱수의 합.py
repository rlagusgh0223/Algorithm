import sys
n = int(sys.stdin.readline())
# 모든 수는 1의 제곱으로 자기 자신까지 더해서 갈 수 있으므로 최댓값은 자기 자신의 수 만큼이다
# ex. 3 = 1^2 + 1^2 + 1^2 으로 제곱수의 합의 최댓값은 3
d = [i for i in range(n+1)]

for i in range(1, n+1):
    # for문에서 i**0.5까지 가게 한다면 int로 만드는 과정에서 값이 부족할 수 있다
    for j in range(1, i):
        if j*j > i:
            break
        if d[i] > d[i-int(j*j)]+1:
            d[i] = d[i-int(j*j)]+1
            # 1부터 시작해서 j의 제곱이 i보다 작은 값이 나오려면 i가 4 이상은 되야한다(4는 2의 제곱)
            # 1의 제곱으로만 더한 경우는 이미 리스트를 작성할때 만들어 뒀으므로 제외
            # ex. n이 7일때 d = [0, 1, 2, 3, 4, 5, 6, 7]
            # d[4] = d[4 - 2*2] + 1 = d[0] + 1 = 1
            # d[5] = d[5 - 2*2] + 1 = d[1] + 1 = 2
            # d[6] = d[6 - 2*2] + 1 = d[2] + 1 = 3
            # d[7] = d[7 - 2*2] + 1 = d[3] + 1 = 4
            # j가 3이 되려면 i가 9 이상이어야 한다
        #print(i, j)
print(d[n])     # d 리스트의 마지막은 입력한 값이니까 d의 마지막 출력해야 제곱수의 합이 나온다