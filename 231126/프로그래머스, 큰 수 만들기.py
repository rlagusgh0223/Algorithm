def solution(number, k):
    answer = []
    for num in number:
        # 아직 뺄 수 있는 자릿수가 있고
        # answer에 값이 있으며
        # answer에서 마지막이 지금보다 작다면
        while k>0 and answer and answer[-1]<num:
            # 뺄 수 있는 자릿수를 하나 줄이고
            k -= 1
            # answer에서 이전 값을 뺀다
            # 이렇게 하면 큰 수 부터 앞으로 오게 할 수 있다
            answer.pop()
        answer.append(num)
    # 혹시 k가 남아있다면 뒤에자리에서 끊는다
    # 앞에서부터 큰 수가 오도록 했기 때문에
    # ex) 100의자리 9를 살리는게
    # 1의자리 9를 살리는거보다 큰 값을 유지할 수 있다
    return ''.join(answer[:len(answer)-k])


import sys
n = sys.stdin.readline().strip()
k = int(sys.stdin.readline())
print(solution(n, k))