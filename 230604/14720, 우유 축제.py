import sys
N = int(sys.stdin.readline())
milk = list(map(int, sys.stdin.readline().split()))
ans = cnt = 0
for now in milk:
    if ans == now: # 여기서 ans 대신 (cnt+1)%3을 하면 코드가 더 짦아지지만 이게 내 코드고 그렇게 크게 차이도 안 나는거 같으니 이걸 남긴다
        ans = (ans+1)%3
        cnt += 1
print(cnt)