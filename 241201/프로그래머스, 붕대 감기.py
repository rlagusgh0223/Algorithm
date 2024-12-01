def solution(bandage, health, attacks):
    attack_time = [a[0] for a in attacks]
    time = max(attack_time) + 1
    check = 0
    max_health = health
    for i in range(time):
        if i in attack_time:
            idx = attack_time.index(i)
            check = 0
            health -= attacks[idx][1]
        else:
            check += 1
            if check == bandage[0]:
                health += bandage[2]
                check = 0
            health = min(max_health, health+bandage[1])
        if health <= 0:
            return -1
    return health

import sys

b = list(map(int, sys.stdin.readline().split(', ')))
h = int(sys.stdin.readline())
at = list(sys.stdin.readline().strip().split('], ['))
at = [list(map(int, a.split(", "))) for a in at]
print(solution(b, h, at))