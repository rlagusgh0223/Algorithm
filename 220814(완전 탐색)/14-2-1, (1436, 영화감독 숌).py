N = int(input())
turn = 665
while N > 0:
    turn += 1
    if '666' in str(turn):
        N -= 1
print(turn)