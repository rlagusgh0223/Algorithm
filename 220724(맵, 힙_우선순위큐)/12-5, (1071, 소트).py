N = int(input())    # n개의 정수를 변수 csort에 계수정렬
csort = [0 for i in range(1002)]
nums = [int(x) for x in input().split()]
for i in range(N):
    csort[nums[i]] += 1

answer =''
while True:    # 종료 시점까지 while문을 계속 돌린다
    tof = False
    for i in range(1001):    # 0~1000까지 for문을 탐색한다
        if csort[i]:    # 해당 계수 i에 해당하는 csort[i]가 존재할때
            tof = True
            if csort[i+1]:    # 계수 i+1에 해당하는 csort[i+1]이 존재한다면
                k = -1    # 계수 i+2 이상의 k값이 csort[k]에 존재하는지 확인하고
                for j in range(i+2, 1001):
                    if csort[j]:
                        k = j
                        break
                if k != -1:    # csort[k]가 존재한다면
                    while csort[i]:    # csort[i]값을 전부 출력하고, scort[k]를 한번 출력한다
                        answer += str(i) + ' '
                        csort[i] -= 1
                    answer += str(k) + ' '
                    csort[j] -= 1
                    break
                else:    # csort[k]가 존재하지 않는다면
                    answer += str(i+1) + ' '    # csort[i+1]의 값을 한번 출력한다
                    csort[i+1] -= 1
                    break
            else:    # 계수 i+1에 해당하는 csort[i+1]이 존재하지 않는다면
                while csort[i]:    # csort[i]를 전부 출력한다
                    answer += str(i) + ' '
                    csort[i] -= 1
                break
        if tof == False:    # 더이상 배열에 수가 남아 있지 않다면 while문을 종료한다
            break

print(answer)