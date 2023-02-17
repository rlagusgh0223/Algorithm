import sys
P = int(sys.stdin.readline())
for _ in range(P):
    coin = sys.stdin.readline().rstrip()
    ans = {"TTT":0, "TTH":0, "THT":0, "THH":0, "HTT":0, "HTH":0, "HHT":0, "HHH":0}
    for i in range(38):
        ans[coin[i:i+3]] += 1
    print(*ans.values())