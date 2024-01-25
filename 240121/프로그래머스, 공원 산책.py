def solution(park, routes):
    routes = [route.split() for route in routes]
    for i in range(len(park)):
        for j in range(len(park[i])):
            if park[i][j] == 'S':
                x, y = i, j

    for op, n in routes:
        ck = True
        if op == 'N':
            nx = x - int(n)
            if 0<=nx<len(park):
                for i in range(x, nx-1, -1):
                    if park[i][y] == 'X':
                        ck = False
                        break
                if ck:
                    x = nx
        elif op == 'S':
            nx = x + int(n)
            if 0<=nx<len(park):
                for i in range(x, nx+1):
                    if park[i][y] == 'X':
                        ck = False
                        break
                if ck:
                    x = nx
        elif op == 'W':
            ny = y - int(n)
            if 0<=ny<len(park[x]):
                for i in range(y, ny-1, -1):
                    if park[x][i] == 'X':
                        ck = False
                        break
                if ck:
                    y = ny
        else:
            ny = y + int(n)
            if 0<=ny<len(park[x]):
                for i in range(y, ny+1):
                    if park[x][i] == 'X':
                        ck = False
                        break
                if ck:
                    y = ny
    return [x, y]


import sys
park = list(sys.stdin.readline().strip().split('","'))
routes = list(sys.stdin.readline().strip().split('","'))
print(solution(park, routes))