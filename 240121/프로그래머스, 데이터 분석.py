def solution(data, ext, val_ext, sort_by):
    answer = []
    ext = ['code', 'date', 'maximum', 'remain'].index(ext)
    sort_by = ['code', 'date', 'maximum', 'remain'].index(sort_by)
    for i in range(len(data)):
        if data[i][ext] < val_ext:
            answer.append(data[i])
    answer.sort(key=lambda x:x[sort_by])
    return answer

import sys
data = list(sys.stdin.readline().strip().split("], ["))
data = [list(map(int, data[i].split(", "))) for i in range(len(data))]
e = sys.stdin.readline().strip()
v = int(sys.stdin.readline())
s = sys.stdin.readline().strip()
print(solution(data, e, v, s))