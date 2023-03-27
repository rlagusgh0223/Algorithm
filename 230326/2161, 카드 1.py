import sys
card = list(range(1, int(sys.stdin.readline())+1))
ans = []
while len(card) > 1:
    ans.append(card.pop(0))
    card.append(card.pop(0))
    # 아래가 내 코드인데 내 코드보다 위의 코드가 더 간단해서 남긴다
    # append()에 del을 넣으려고 해서 안되가지고 아래 식으로 했는데
    # pop()을 이용하면 되는거였다.
    # n1, n2 = card[0], card[1]
    # ans.append(n1)
    # del card[0:2]
    # card.append(n2)
ans.append(card.pop(0))
print(*ans)