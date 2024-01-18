def solution(numbers, hand):
    answer = ''
    pad = {'1':(0,0), '2':(0,1), '3':(0,2),
           '4':(1,0), '5':(1,1), '6':(1,2),
           '7':(2,0), '8':(2,1), '9':(2,2),
           '*':(3,0), '0':(3,1), '#':(3,2)
    }
    l, r = pad['*'], pad['#']
    for num in numbers:
        if num in [1, 4, 7]:
            answer += 'L'
            l = pad[str(num)]
        elif num in [3, 6, 9]:
            answer += 'R'
            r = pad[str(num)]
        else:
            left = abs(l[0]-pad[str(num)][0]) + abs(l[1]-pad[str(num)][1])
            right = abs(r[0]-pad[str(num)][0]) + abs(r[1]-pad[str(num)][1])
            if left > right:
                answer += 'R'
                r = pad[str(num)]
            elif left < right:
                answer += 'L'
                l = pad[str(num)]
            else:
                if hand == 'left':
                    answer += 'L'
                    l = pad[str(num)]
                else:
                    answer += 'R'
                    r = pad[str(num)]
    return answer

import sys
num = list(map(int, sys.stdin.readline().split(", ")))
hand = sys.stdin.readline().strip()
print(solution(num, hand))