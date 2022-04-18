import sys
N, K = map(int, sys.stdin.readline().split())
number = list(map(int, sys.stdin.readline().rstrip()))
cntList = [0] * K    # 지워야할 K개의 수를 담는 리스트
cnt = 0    # cnt의 위치를 나타내는 변수
k = K    # K개의 개수를 두번 카운트 해야 되서 다른 변수로도 만듦

# 가장 큰 수를 만들기 위해서는 왼쪽에 있는 수가 커야 한다
for i in range(1, len(number)):
    if number[i-1] < number[i]:    # 왼쪽에 있는 수가 더 크고 아직 다 지우지 않았다면
        cntList[cnt] = i-1    # 바로 지우면 
        k -= 1
        cnt += 1
        if k == 0:
            break

for i in cntList:
    number[i] = 0

for i in number:
    if i == 0:    # K번째 까지의 0인 수는 출력하지 않는다(혹시 0을 입력했을 가능성 고려)
        if K > 0:
            continue
        K -= 1    # K번째 까지의 수 중 0인 수는 어차피 0으로 입력했다고 해도 크기를 고려해서 없애는게 맞다

    print(i, end='')