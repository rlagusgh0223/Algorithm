def solution(arr):
    answer = []
    for a in arr:
        # if answer[-1:] == [a]:  <- 이런 방법도 있다
        # answer[-1:]로 하면 answer의 마지막 값을 리스트로 만드므로
        # answer가 비어있다면 []로 만들어진다
        # 단, 이 경우에는 리스트로 만들어지므로 비교할 문자도 리스트로 만들어야 된다
        if len(answer)==0 or answer[-1]!=a:
            answer.append(a)
    return answer


import sys
arr = list(map(int, sys.stdin.readline().strip().split(",")))
print(solution(arr))