def solution(picks, minerals):
    answer = 0

    pick = sum(picks)
    if len(minerals) > pick:
        minerals = minerals[:pick*5]
    
    now = [[0, 0, 0] for _ in range((len(minerals)//5) + 1)]
    for i in range(len(minerals)):
        if minerals[i] == 'diamond':
            now[i//5][0] += 1
        elif minerals[i] == 'iron':
            now[i//5][1] += 1
        else:
            now[i//5][2] += 1
    
    now.sort(key=lambda x:(-x[0], -x[1], -x[2]))

    for dia, iron, stone in now:
        for i in range(len(picks)):
            if picks[i]>0 and i==0:
                answer += dia + iron + stone
                picks[i] -= 1
                break
            if picks[i]>0 and i==1:
                answer += (dia*5) + iron + stone
                picks[i] -= 1
                break
            if picks[i]>0 and i==2:
                answer += (dia*25) + (iron*5) + stone
                picks[i] -= 1
                break

    return answer


import sys

picks = list(map(int, sys.stdin.readline().split(", ")))
minerals = list(sys.stdin.readline().strip().split('", "'))
print(solution(picks, minerals))