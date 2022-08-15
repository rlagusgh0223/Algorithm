import sys

def DFS(index, sum):
    global maxAns, minAns
    if index == N-1:
        if maxAns < sum:
            maxAns = sum
        if minAns > sum:
            minAns = sum
        return
    for i in range(4):
        temp = sum
        if operator[i] == 0:
            continue
        if i == 0:
            sum += numArr[index+1]
        elif i==1:
            sum -= numArr[index+1]
        elif i==2:
            sum *= numArr[index+1]
        else:
            if sum<0:
                sum = abs(sum)//numArr[index+1]*-1
            else:
                sum //= numArr[index+1]
        operator[i] -= 1
        DFS(index+1, sum)
        operator[i] += 1
        sum = temp

N = int(sys.stdin.readline())
numArr = list(map(int, sys.stdin.readline().split()))
operator = list(map(int, sys.stdin.readline().split()))
maxAns = float('-Inf')
minAns = float('Inf')
DFS(0, numArr[0])
print(maxAns)
print(minAns)