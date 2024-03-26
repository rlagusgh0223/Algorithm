from itertools import permutations


def solutions(spell, dic):
    check = list(permutations(spell, len(spell)))
    check = [''.join(ck) for ck in check]
    for ck in check:
        if ck in dic:
            return 1
    return 2

# 이 코드가 더 빠르고 간편하다
def solution(spell, dic):
    spell = set(spell)
    for d in dic:
        if len(spell - set(d)) == 0:
            return 1
    return 2

import sys

spell = list(sys.stdin.readline().strip().split('", "'))
dic = list(sys.stdin.readline().strip().split('", "'))
print(solution(spell, dic))