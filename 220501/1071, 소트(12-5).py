# 모범답안
N = int(input())
csort = [0 for i in range(1002)]
nums = [int(x) for x in input().split()]
for i in range(N):
    csort[nums[i]] += 1

answer = ''
while True:
    tof = False
    for i in range(1001):
        if csort[i]:    # 0 ~ 1000까지의 수 중 csort[]가 존재할때
            tof = True
            if csort[i+1]:    # 그 수 + 1에 해당하는 csort가 존재한다면
                k = -1
                for j in range(i+2, 1001):    # 계수 i+2 이상의 값이 csort[k]에 존재하는지 확인하고
                    if csort[j]:
                        k = j
                        break
                if k != -1:    # csort[k]가 존재한다면
                    while csort[i]:    # csort[i]값을 전부 출력하고, csort[k]를 한번 출력한다
                        answer += str(i)+' '
                        csort[i] -= 1
                    answer += str(k)+' '
                    csort[k] -= 1
                    break
                else:    # csort[k]가 존재하지 않는다면
                    answer += str(i+1)+' '    # csort[i+1]의 값을 한번 출력한다
                    csort[i+1] -= 1
                    break
            else:    # 계수 i+1에 해당하는 csort[i+1]이 존재하지 않는다면
                while csort[i]:    # csort[i]를 전부 출력한다
                    answer += str(i)+' '
                    csort[i] -= 1
                break
    if tof == False:    # 배열에 더 이상 수가 남아있지 않다면 while문을 종료한다
        break

print(answer)