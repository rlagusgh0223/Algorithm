cup = [1, 0, 0, 2]
change = list(input())
for now in change:
    if now == 'A':
        cup[0], cup[1] = cup[1], cup[0]
    elif now == 'B':
        cup[0], cup[2] = cup[2], cup[0]
    elif now == 'C':
        cup[0], cup[3] = cup[3], cup[0]
    elif now == 'D':
        cup[1], cup[2] = cup[2], cup[1]
    elif now == 'E':
        cup[1], cup[3] = cup[3], cup[1]
    else:
        cup[2], cup[3] = cup[3], cup[2]
print(cup.index(1)+1)
print(cup.index(2)+1)