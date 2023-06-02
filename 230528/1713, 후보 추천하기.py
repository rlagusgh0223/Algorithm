import sys
N = int(sys.stdin.readline())
n = int(sys.stdin.readline())
student = list(map(int, sys.stdin.readline().split()))
ans = []  # 최종 후보
cnt = []  # 후보들의 추천 수
for now in student:
    if now in ans:  # 후보 명단에 있는 추천인이라면
        cnt[ans.index(now)] += 1  # 추천 수 증가
    else:  # 후보 명단에 없다면
        if len(ans) >= N:  # 후보 인원이 초과되면
            # 추천 수가 적은 녀석(추천수가 같다면 가장 오래된 추천인)을 지운다
            ck = cnt.index(min(cnt))
            del ans[ck]
            del cnt[ck]
        ans.append(now)  # 새 후보를 추가하고, 최초이므로 추천수는 1로 입력한다
        cnt.append(1)
ans.sort()
print(*ans)