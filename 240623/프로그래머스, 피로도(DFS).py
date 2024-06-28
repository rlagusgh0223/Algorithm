def solution(k, dungeons):
    answer = 0
    check = [0] * len(dungeons)

    def DFS(k, cnt, dungeons):
        # answer 변수는 외부에서 선언했으므로
        # DFS함수 내부에서 쓰기 위해서는 nonlocal을 써야 한다
        # global은 전역변수이고,
        # nonlocal은 중첩된 함수에서 부모 함수의 변수를 수정할 때 사용된다
        nonlocal answer  
        answer = max(answer, cnt)
        for i in range(len(dungeons)):
            # 최소 필요 피로도 이상을 가지고 있고 방문한 적이 없는 던전이라면 계산한다
            if k>=dungeons[i][0] and check[i]==0:
                check[i] = 1
                DFS(k-dungeons[i][1], cnt+1, dungeons)
                check[i] = 0

    # 사실 기존의 풀이와 별 차이 없는데 DFS를 solution안에 넣어봤다
    # 그냥 answer랑 check를 전역변수로 선언하지 않은것만 다르다
    DFS(k, 0, dungeons)  # 남은 피로도, 깬 던전의 수, 던전의 종류

    return answer

import sys

k = int(sys.stdin.readline())
dungeons = list(sys.stdin.readline().strip().split("],["))
dungeons = [list(map(int, d.split(","))) for d in dungeons]
print(solution(k, dungeons))