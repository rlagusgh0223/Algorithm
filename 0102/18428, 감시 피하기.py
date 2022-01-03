from collections import deque
import sys

graph = []          # 전반적인 위치 받을 리스트
ans = 0
t = []              # 선생님 위치 받는 리스트
s = []              # 학생 위치 받는 리스트
tCnt = 0            # 선생님 수 카운트 하는 변수
endFlag = False
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
N = int(sys.stdin.readline())

for i in range(N):
    graph.append(list(sys.stdin.readline().split()))    # 그래프 입력
    for j in range(len(graph[i])):                      # 그래프에 T가 있으면
        if graph[i][j] == 'T':                          # 리스트에 선생님 위치 입력하고 선생님 수 증가
            t.append([i,j])
            tCnt+=1

def search():                           # 학생을 만나면 0을 리턴, 벽을 만나거나 아무것도 없으면 1을 리턴
    global tCnt
    for i in range(tCnt):               # 선생님 수 만큼 반복
        r = t[i][0]                     # 해당 턴 선생님 x좌표
        c = t[i][1]                     # 해당 턴 선생님 y좌표
        for k in range(4):              # 방향선택
            nr = r+dx[k]
            nc = c+dy[k]
            while 0<=nr<N and 0<=nc<N:  # 선생님 위치에서부터 그래프 끝날때까지 탐색하는 스킬 -> 스킬 3
                if graph[nr][nc]=='S':
                    return 0
                elif graph[nr][nc]=='O':
                    break
                nr = nr+dx[k]
                nc = nc+dy[k]
    return 1

def recurrsive(x, y, depth):              # 벽을 3개 세우는 역할 왼쪽위부터 오른쪽 아래까지 전부 다 
    global N, ans
    if ans == 1:                          # 학생과 접촉하지 않은 경우 끝(리턴)
        return
    if depth == 3:      # 종료조건 : 스킬2
                        # 이 순간까지 왔다는건 벽 3개가 다 세워져서 이제 그냥 선생님이 '해당 맵'(우리가 만든)에서
                        # 학생을 감시 할수 있는지 확인을 하면됨 
        if search()==1:                 # 학생과 접촉하지 않으면 ans = 1
            ans = 1
        return
    tmp = 0
    for i in range(x,N):
        for j in range(N):              # x, y를 어떤 방식이든 넘겨줘야함 -> 스킬 1
            if tmp == 0:                # 처음에 j는 y부터 시작, 그 다음줄은 0부터 시작하게 하고싶어서
                tmp = 1
                j = y
                if j>=N:
                    break
            if graph[i][j]=='X':
                graph[i][j] = 'O'
                recurrsive(i, j+1, depth+1)     # depth를 넣은 재귀함수 -> 스킬 2
                graph[i][j] = 'X'


for x, y in t:                      # S 와 T가 바로 붙어있으면 무조건 걸리므로 endFlag = True하여
    for i in range(4):              # 다음 연산 자동으로 안하게 한다
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < N:
            if graph[nx][ny] == 'S':
                endFlag = True
                break
    if endFlag:
        break

if not endFlag:                     # 선생님과 학생이 바로 붙어있지 않다면 학생과 벽 관계 파악
    recurrsive(0,0,0)


if endFlag or ans==0:               # 선생님과 학생이 바로 붙어있거나 선생님의 경로에 학생이 있다면 NO 출력
    print("NO")
else:
    print("YES")




