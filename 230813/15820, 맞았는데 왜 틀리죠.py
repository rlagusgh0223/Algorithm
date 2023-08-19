# 맞았는데 50점이라고 나온다
# 인터넷에 있는 다른 코드도 50점이라고 나오는거 봐서
# 이 문제는 만점이 50점인 것 같다
# 서브태스크도 다 맞았다고 나온다
import sys
S1, S2 = map(int, sys.stdin.readline().split())
ans = "Accepted"
for _ in range(S1):
    st, m = map(int, sys.stdin.readline().split())
    if st != m:
        ans = "Wrong Answer"
for _ in range(S2):
    st, m = map(int, sys.stdin.readline().split())
    if st != m and ans == "Accepted":
        ans = "Why Wrong!!!"
print(ans)