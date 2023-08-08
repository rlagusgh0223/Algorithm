import sys
T = int(sys.stdin.readline())
for i in range(1, T+1):
    gan = list(map(int, sys.stdin.readline().split()))
    sa = list(map(int, sys.stdin.readline().split()))
    gan[1] *= 2
    gan[2] *= 3
    gan[3] *= 3
    gan[4] *= 4
    gan[5] *= 10
    sa[1] *= 2
    sa[2] *= 2
    sa[3] *= 2
    sa[4] *= 3
    sa[5] *= 5
    sa[6] *= 10
    if sum(gan) > sum(sa):
        print("Battle {}: Good triumphs over Evil".format(i))
    elif sum(gan) < sum(sa):
        print("Battle {}: Evil eradicates all trace of Good".format(i))
    else:
        print("Battle {}: No victor on this battle field".format(i))