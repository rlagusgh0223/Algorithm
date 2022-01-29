# 모범답안을 한번 한 후 내가 만든 답안
import sys
n = int(sys.stdin.readline())
data = list(map(int, sys.stdin.readline().split()))
add, miu, sub, div = map(int, sys.stdin.readline().split())

max_value = -1e9
min_value = 1e9

def DFS(i, now):
    global n, max_value, min_value, add, miu, sub, div
    if i == n:
        max_value = max(max_value, now)
        min_value = min(min_value, now)
    else:
        if add > 0:
            add -= 1
            DFS(i+1, now + data[i])
            add += 1
        if miu > 0:
            miu -= 1
            DFS(i+1, now - data[i])
            miu += 1
        if sub > 0:
            sub -= 1
            DFS(i+1, now * data[i])
            sub += 1
        if div > 0:
            div -= 1
            DFS(i+1, int(now / data[i]))    # 이 부분 now//data[i]로 하면 틀렸다고 나온다
            div += 1

DFS(1, data[0])
print(max_value)
print(min_value)




###########################################
"""
# 모범답안
import sys
n = int(sys.stdin.readline())
# 연산을 수행하고자 하는 수 리스트
data = list(map(int, sys.stdin.readline().split()))
# 더하기, 빼기, 곱하기, 나누기 연산자 개수
add, sub, mul, div = map(int, sys.stdin.readline().split())

# 최솟값과 최댓값 초기화
min_value = 1e9    # 1e9는 1 * 10^9을 의미한다
max_value = -1e9

# DFS 메서드
def DFS(i, now):
    global min_value, max_value, add, sub, mul, div
    #print("i : {}, now : {}".format(i,now))
    #print(add, sub, mul, div)
    # 모든 연산자를 다 사용한 경우, 최솟값과 최댓값 업데이트
    if i == n:
        min_value = min(min_value, now)
        max_value = max(max_value, now)
    else:
        # 각 연산자에 대하여 재귀적으로 수행
        if add > 0:
            add -= 1
            DFS(i+1, now + data[i])
            add += 1
        if sub > 0:
            sub -= 1
            DFS(i+1, now - data[i])
            sub += 1
        if mul > 0:
            mul -= 1
            DFS(i+1, now * data[i])
            mul += 1
        if div > 0:
            div -= 1
            DFS(i+1, int(now/data[i]))
            div += 1
    #print('=============')

# DFS 메서드 호출
DFS(1, data[0])

# 최댓값과 최솟값 출력
print(max_value)
print(min_value)
"""