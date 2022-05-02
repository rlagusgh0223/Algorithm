# 설명을 봐도 무슨 말인지 모르겠다
# 나중에 다시 봐야겠다
import sys

q, x = map(int, sys.stdin.readline().split())
map = {}
mex = 0
for _ in range(q):
    y = int(sys.stdin.readline())
    if y%x in map:    # map에 y%x를 key로 하는 값이 있다면 그 key값의 value는 1 증가한다(13번째줄)
        if y%x + x*map[y%x] in map:
            map[y%x + x*map[y%x]] += 1
        else:
            map[y%x + x*map[y%x]] = 1
        map[y%x] += 1
    else:
        map[y%x] = 1

    while mex in map:
        mex += 1
    print(mex)