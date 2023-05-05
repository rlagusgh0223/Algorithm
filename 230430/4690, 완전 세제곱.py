Cube, Triple = [], []
for a in range(2, 101):
    for b in range(2, a):
        for c in range(b+1, 101):
            for d in range(c+1, 101):
                if a**3 == b**3 + c**3 + d**3:
                    Cube.append(a)
                    Triple.append([b,c,d])
for i in range(len(Cube)):
    print("Cube = {}, Triple = ({},{},{})".format(Cube[i], Triple[i][0], Triple[i][1], Triple[i][2]))