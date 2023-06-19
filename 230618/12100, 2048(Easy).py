def rotate(B, N):  # 오른쪽으로 90도 돌린다(상, 하, 좌, 우로 검사하기 위해 사용)
    NB = deepcopy(B)
    for i in range(N):
        for j in range(N):
            NB[j][N-1-i] = B[i][j]
    return NB

def convert(lst, N):  # lst는 Board에서 한 줄만 들어온거다
    new_list = [i for i in lst if i>0]  # i가 0인 경우(공백)는 입력하지 않아 숫자가 있는 칸들이 끝까지 가게 한다
    for i in range(1, len(new_list)):  # 앞의 칸과 지금 칸의 값이 같으면 하나로 합치고 지금 칸은 빈칸으로 남긴다
        if new_list[i-1] == new_list[i]:
            new_list[i-1] *= 2
            new_list[i] = 0
    new_list = [i for i in new_list if i>0]
    return new_list+[0]*(N-len(new_list))  # 한쪽으로 쏠린 리스트 한 줄에 대해 남는 구역은 0으로 리스트를 채운다

def DFS(N, B, count):
    ret = max([max(i) for i in B])  # Board에서 가장 큰 값 찾는다
    if count == 0:  # 최대 5번 이동해서 만들 수 있는 가장 큰 블록의 값 반환
        return ret  # 상, 하, 좌, 우 5번을 하므로 4**5 = 1024로 시간복잡도 문제 없다
    for _ in range(4):  # 상, 하, 좌, 우를 돌려보므로 4번
        X = [convert(i, N) for i in B]  # Board에서 각 줄을 합칠 수 있는건 합친 리스트
        if X != B:  # 처음 주어진 Board와 차이가 있다면
            ret = max(ret, DFS(N, X, count-1))  # 변경된 값에 맞춰 다음 탐색도 하고 그 중 최댓값을 찾는다
        B = rotate(B, N)  # 상, 하, 좌, 우로 돌려보기 위해 우측으로 90도 돌린 값을 입력받는다
    return ret

from copy import deepcopy
import sys
N = int(sys.stdin.readline())
Board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
print(DFS(N, Board, 5))