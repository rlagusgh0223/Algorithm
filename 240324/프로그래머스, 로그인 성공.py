def solution(id_pw, db):
    if id_pw in db:
        return 'login'
    else:
        for d, b in db:
            if id_pw[0]==d and id_pw[1]!=b:
                return 'wrong pw'
    return 'fail'

import sys

id_pw = list(sys.stdin.readline().strip().split('", "'))
db = list(sys.stdin.readline().strip().split('"], ["'))
db = [list(d.split('", "')) for d in db]
print(solution(id_pw, db))