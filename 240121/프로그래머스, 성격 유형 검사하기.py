def solution(survey, choices):
    answer = ''
    case = {'R':0, 'T':0, 'C':0, 'F':0,
            'J':0, 'M':0, 'A':0, 'N':0}
    for now in range(len(choices)):
        if choices[now] >= 4:
            case[survey[now][1]] += (choices[now] - 4)
        else:
            case[survey[now][0]] += (4 - choices[now])
    for i in range(0, 7, 2):
        if case[list(case)[i]] < case[list(case)[i+1]]:
            answer += list(case)[i+1]
        else:
            answer += list(case)[i]
    return answer


import sys
survey = list(sys.stdin.readline().strip().split('", "'))
choices = list(map(int, sys.stdin.readline().split(', ')))
print(solution(survey, choices))