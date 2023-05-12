# P : 랭킹리스트에 들어갈 수 있는 점수의 개수
# N : 현재 노래의 개수
# 거기에 내 점수가 추가되었을때 나는 몇등인가?
# 말 참 어렵게 썼다....
import sys
N, score, P = map(int, sys.stdin.readline().split())
if N == 0:  # N이 0이면 리스트에 들어있는게 없으므로 무조건 1등이다(P는 10이상)
    print("1")
    exit()
lst = sorted(list(map(int, sys.stdin.readline().split()))+[score], reverse=True)
if N==P and lst[-1]>=score:  # 이미 리스트에 노래가 가득 차 있었고 내 점수가 최하점과 같다면 내 점수는 리스트에 들어가지 못한다
    print("-1")
else:
    print(lst.index(score)+1)