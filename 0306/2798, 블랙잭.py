import sys

# 문제에서 입력한 값들을 받을 변수 밑 리스트
n, m = map(int, sys.stdin.readline().split())
lst = list(map(int, sys.stdin.readline().split()))

max_sum = 0    # 가장 합당한 값을 저장하는 변수

for i in lst:    # 카드 3장을 더하라고 했으니 3차원 배열 이용한다(3차원 배열이라 시간초과가 날거라고 생각했는데 아닌가보다)
    for j in lst:
        if i == j:    # 같은 리스트를 사용하므로 같은 수가 나올 경우 진행하지 않는다
            continue
        for k in lst:
            if i == k or j == k:
                continue
            elif max_sum < i+j+k <= m:    # 이전에 값보다 크면서 최댓값을 넘지 않는값을 찾아 저장한다
                max_sum = i+j+k

print(max_sum)