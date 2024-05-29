# 행렬 dp[s][e]를 구할때 점화식
# dp[s][m] + sp[m+1][e] + sizes[s][0]*sizes[m][1]*sizes[e][1]
# m은 s <= m < e 인 모든 수를 의미한다
# 문제는 최적의 행렬 곱셈이므로 이렇게 나온 곱셈의 수 중 가장 작은 값을 구하면 된다
def solution(sizes):
    dp = [[0]*len(sizes) for _ in range(len(sizes))]
    for gap in range(1, len(sizes)):
        for s in range(len(sizes)-gap):
            e = s + gap
            lst = []
            for m in range(s, e):
                lst.append(dp[s][m] + dp[m+1][e] + sizes[s][0]*sizes[m][1]*sizes[e][1])
            dp[s][e] = min(lst)
    return dp[0][-1]



import sys

sizes = list(sys.stdin.readline().strip().split("],["))
sizes = [list(map(int, s.split(","))) for s in sizes]
print(solution(sizes))