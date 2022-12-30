# 0 : 정보과학관
# 1 : 전산관
# 2 : 미래관
# 3 : 신양관
# 4 : 한경직기념관
# 5 : 진리관
# 6 : 학생회관
# 7 : 형남공학관
def nxt(state):
    tmp = [0 for _ in range(8)]
    tmp[0] = state[1] + state[2]
    tmp[1] = state[0] + state[2] + state[3]
    tmp[2] = state[0] + state[1] + state[3] + state[4]
    tmp[3] = state[1] + state[2] + state[4] + state[5]
    tmp[4] = state[2] + state[3] + state[5] + state[7]
    tmp[5] = state[3] + state[4] + state[6]
    tmp[6] = state[5] + state[7]
    tmp[7] = state[4] + state[6]
    for i in range(8):
        tmp[i] %= 1000000007
    return tmp

DP = [1, 0, 0, 0, 0, 0, 0, 0]
D = int(input())
for _ in range(D):
    DP = nxt(DP)
print(DP[0])