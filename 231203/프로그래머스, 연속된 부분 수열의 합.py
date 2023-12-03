def solution(sequence, k):
    answer = []
    K = 0  # 부분수열의 합
    start = 0  # 부분수열의 출발점
    end = -1  # 부분수열의 도착점
    while True:
        # 아직 부분수열의 합이 k보다 작으면 뒤의 수열을 더한다
        if K < k:
            end += 1
            # 만약 뒤의 수열이 없으면 종료
            if end >= len(sequence):
                break
            K += sequence[end]

        # 지금 부분수열의 합이 k 이상이면 맨 앞의 수열을 뺀다
        else:
            K -= sequence[start]
            # 부분수열의 시작점이 전체 수열의 마지막이면 종료
            if start >= len(sequence):
                break
            start += 1

        # 지금까지의 부분수열의 합이 k이면 answer에 출발점, 도착점 입력
        if K == k:
            answer.append([start, end])
    # end-start 즉, 도착점과 출발점의 길이가 짧은 순서대로 정렬
    answer.sort(key=lambda x:x[1]-x[0])
    return answer[0]


import sys
sequence = list(map(int, sys.stdin.readline().split(", ")))
k = int(sys.stdin.readline())
print(solution(sequence, k))