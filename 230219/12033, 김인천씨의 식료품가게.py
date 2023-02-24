# 똑같은 결과일 것 같은데 반복문이 ans의 숫자 갯수가 N이 될때까지 돌아가게 하는건 되고
# for로 lst에서 하나씩 뽑아서 비교한 후 ans에 입력하는건 안된다
import sys
T = int(sys.stdin.readline())
for i in range(T):
    N = int(sys.stdin.readline())
    lst = list(map(int, sys.stdin.readline().split()))
    ans = []
    while len(ans) != N:
        now = lst.pop()
        if now*0.75 in lst:
            ans.append(int(now*0.75))
            del lst[lst.index(now*0.75)]
    ans.sort()
    print("Case #{}: {}".format(i+1, ' '.join(map(str, ans))))