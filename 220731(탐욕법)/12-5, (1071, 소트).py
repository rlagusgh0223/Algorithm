N = int(input())
csort = [0 for _ in range(1002)]
nums = list(map(int, input().split()))
for i in range(N):
    csort[nums[i]] += 1

answer = ''
while True:
    tof = True
    for i in range(1001):
        if csort[i]:
            tof = False
            if csort[i+1]:
                k = -1
                for j in range(i+2, 1001):
                    if csort[j]:
                        k = j
                        break
                if k != -1:
                    while csort[i]:
                        answer += str(i)+' '
                        csort[i] -= 1
                    answer += str(k)+' '
                    csort[k] -= 1
                    break
                else:
                    answer += str(i+1)+' '
                    csort[i+1] -= 1
                    break
            else:
                while csort[i]:
                    answer += str(i)+' '
                    csort[i] -= 1
                break
    if tof:
        break

print(answer)