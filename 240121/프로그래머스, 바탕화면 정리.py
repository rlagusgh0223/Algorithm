# 모범답안
def solution(wallpaper):
    x, y = [], []
    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[i])):
            if wallpaper[i][j] == '#':
                x.append(i)
                y.append(j)
    return [min(x), min(y), max(x)+1, max(y)+1]


# def solutions(wallpaper):
#     answer = [len(wallpaper), len(wallpaper[0]), 0, 0]
#     for i in range(len(wallpaper)):
#         for j in range(len(wallpaper[i])):
#             if wallpaper[i][j] == '#':
#                 if i < answer[0]:
#                     answer[0] = i
#                 if j < answer[1]:
#                     answer[1]  = j
#                 if i+1 > answer[2]:
#                     answer[2] = i+1
#                 if j+1 > answer[3]:
#                     answer[3] = j+1
#     return answer


import sys
wall = list(sys.stdin.readline().strip().split('", "'))
print(solution(wall))