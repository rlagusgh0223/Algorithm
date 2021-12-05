import sys
n = int(sys.stdin.readline())
cnt = 0

check_row = [0 for _ in range(n)]
check_col = [0 for _ in range(n)]
check_dae = [0 for _ in range(2*n)]
check_dae2 = [0 for _ in range(2*n)]

def go(r, c):
    check_row[r] = 1
    check_col[c] = 1
    check_dae[r-c+n] = 1
    check_dae2[r+c] = 1

def ungo(r, c):
    check_row[r] = 0
    check_col[c] = 0
    check_dae[r-c+n] = 0
    check_dae2[r+c] = 0

def dfs(depth):
    global cnt
    if depth == n:
        cnt += 1
        return

    for j in range(n):
        if check_row[depth] == 0 and check_col[j] == 0 and check_dae[depth-j+n] == 0 and check_dae2[depth+j] == 0:
            go(depth, j)
            dfs(depth+1)
            ungo(depth, j)

dfs(0)
print(cnt)

"""
##########################################
#참고하기 위해 전에 올렸던 코드에 주석을 달았다
import sys

def check(x):   #대각선으로 퀸이 있는지 확인
    for i in range(x):
        if co[x] == co[i] or abs(co[i]-co[x]) == x-i:
            return False
    return True

def dfs(x): #0을 받고 시작
    global res    #함수 밖에 있는 res 접근
    if x == n:    #이번이 마지막이라면
        res += 1    #1 더한다?
        return
    for i in range(n):  #0 ~ n-1까지 반복
        co[x] = i    #0으로 채워진 15개의 리스트 중 현재 행의 값을 
        if check(x):    #check의 값이 True면 수행, False면 안함
            dfs(x+1)    #재귀함수 이용하여 다음 수로 넘어감

n = int(sys.stdin.readline())
res = 0    #퀸이 있는 경우의 수를 세기 위한 변수
co = [0] * 15    #0~15까지 받으니 15개의 리스트. 퀸이 있는지 파악하기 위한

dfs(0)    #dfs에 0 넣어서 호출(0이 처음이니까 넣은 듯)
print(res)    #퀸의 개수 출력
"""
