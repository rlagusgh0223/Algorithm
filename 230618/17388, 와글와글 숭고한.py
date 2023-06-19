import sys
S, K, H = map(int, sys.stdin.readline().split())
if S+K+H >= 100:
    print("OK")
elif S == min(S, K, H):
    print("Soongsil")
elif K == min(S, K, H):
    print("Korea")
elif H == min(S, K, H):
    print("Hanyang")