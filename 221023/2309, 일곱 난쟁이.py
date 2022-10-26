import sys
dwarf = [int(sys.stdin.readline()) for _ in range(9)]
dwarf.sort()
total = sum(dwarf)
for i in range(9):
    for j in range(i+1, 9):
        if total - dwarf[i] - dwarf[j] == 100:
            for k in range(9):
                if k==i or k==j:
                    continue
                print(dwarf[k])
            sys.exit(0)  # 이거 안쓰면 틀렸다고 한다