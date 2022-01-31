import sys
x, y, w, h = map(int, sys.stdin.readline().split())

# x, y 는 그 자체로 0, 0에서 얼마나 떨어져 있는지 나타낸다. 그러니까 x, y 중 작은 값이 더 경계선에 가까운 값이다
min_value = min(x,y)
# w-x는 x에서부터 경계선의 거리를 나타내며, w는 반드시 x 이상이므로 abs를 할 필요 없다. x와 w의 거리와 x와 0의 거리 중 짧은 거리 기록
min_value = min(min_value, w-x)
min_value = min(min_value, h-y)

print(min_value)