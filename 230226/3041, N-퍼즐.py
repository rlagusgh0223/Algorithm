# 전체 퍼즐에서 바뀐 퍼즐의 행, 열 위치를 합하면 된다
# ex. 3개의 문자가 대각선으로 한 칸씩 내려가면
# (1,1), (1,1), (1,1)이 증가하여 6이 된다?
num = 0
for i in range(4):
    s = list(input())
    for j in range(4):
        if s[j] != '.':
            num += abs((ord(s[j]) - ord('A'))%4 - j)  # 이동한 열의 위치. ABCD~순서대로니까 A까지빼고 j만큼 빼면 A+j의 알파벳이 된다
            num += abs((ord(s[j]) - ord('A'))//4 - i)  # 이동한 행의 위치
print(num)