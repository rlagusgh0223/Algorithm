def solution(number, k):
    answer = []
    for num in number:
        # 아직 제거할 개수가 있고
        # answer에 수가 있으며
        # 그 수가 지금 수보다 작을 경우
        # 지금 나보다 작은 앞의 수 가능한 다 제거한다
        while k>0 and answer and answer[-1]<num:
            answer.pop()
            k -= 1
        # 현재 수는 앞에 작은 수가 없거나
        # 앞의 작은 수가 있더라도 제거할 수 만큼 제거해
        # 더이상 제거할 수 없는 상태이므로 answer에 입력한다
        answer.append(num)
    # 혹시 k가 남았다면 k만큼 뒤를 자른다
    return ''.join(answer[:len(answer)-k])


import sys

number = sys.stdin.readline().strip()
k = int(sys.stdin.readline())
print(solution(number, k))