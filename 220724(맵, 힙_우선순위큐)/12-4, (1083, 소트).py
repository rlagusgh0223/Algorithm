# 설명이 어려워서 무슨 말인지 모르겠다. 일단 코드부터 외우자
N = int(input())
arr = [int(i) for i in input().split()]

s = int(input())
while True:    # 반복문을 계속 돌린다(맨 왼쪽에 있는 수를 매순간 크게 만들기 위해)
    tof = False    # 종료 지점을 나타내기 위한 변수를 생성한다
    for i in range(N):
        idx = i
        cmp = 0
        for j in range(N-1, i, -1):
            if arr[idx]<arr[j] and j-1<=s:
                idx = j
                tof = True
                cmp = j-1
        if idx != i:
            tmp = arr[idx]
            del arr[idx]
            arr.insert(i, tmp)
            s -= cmp
            break
    if tof == False:    # tof = False라면 바꿀 수를 찾지 못한것이므로 while문 탈출
        break

print(*arr)