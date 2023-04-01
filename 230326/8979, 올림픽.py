import sys
N, K = map(int, sys.stdin.readline().split())
lst = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
# lst[1], lst[2], lst[3] 순으로 내림차순
lst.sort(key = lambda x:(x[1], x[2], x[3]), reverse=True)
# K국가의 등수 확인
for i in range(N):
    if lst[i][0] == K:
        idx = i
# 동일한 점수의 국가가 있는 경우를 대비하여
# 그런데 이렇게 하면 뽑고자 하는 국가보다 점수가 높은 국가 중 중복된 점수의 국가가 있는건 계산 못할텐데
# 그걸 반영한 식을 틀렸다고 하고 이게 맞다고 한다
for i in range(N):
    if lst[i][1:] == lst[idx][1:]:
        print(i+1)
        break