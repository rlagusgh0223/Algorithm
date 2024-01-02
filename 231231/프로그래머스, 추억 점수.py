def solution(name, yearning, photo):
    answer = []
    for ph in photo:
        check = 0
        for p in ph:
            if p in name:
                check += yearning[name.index(p)]
        answer.append(check)
    return answer

import sys
name = list(sys.stdin.readline().strip().split('", "'))
yearning = list(map(int, sys.stdin.readline().split(", ")))
photo = list(sys.stdin.readline().strip().split('"], ["'))
for i in range(len(photo)):
    photo[i] = list(photo[i].split('", "'))
print(solution(name, yearning, photo))

# 예제
# may", "kein", "kain", "radi
# 5, 10, 1, 3
# may", "kein", "kain", "radi"], ["may", "kein", "brin", "deny"], ["kon", "kain", "may", "coni

# kali", "mari", "don
# 11, 1, 55
# kali", "mari", "don"], ["pony", "tom", "teddy"], ["con", "mona", "don

# may", "kein", "kain", "radi
# 5, 10, 1, 3
# may"], ["kein", "deny", "may"], ["kon", "coni