import sys
n, w, l = map(int, sys.stdin.readline().split())
lst = list(map(int, sys.stdin.readline().split()))
cnt = 0  # 총 걸리는 시간을 계산할 변수
ans = [0] * w  # 다리에 올라오는 트럭을 입력할 리스트
while True:  # 모든 트럭이 다리를 건널때까지 반복
    cnt += 1  # 시간은 1초씩 증가
    del ans[0]  # 다리에 있는 첫 값(트럭 또는 0) 삭제(l은 1 이상이므로 ans가 없을리는 없다)
    # 아직 다리를 건너지 않은 트럭이 있고 그 중 첫 트럭과 다리에 있는 트럭의 합이 다리가 견딜수 있는 하중 이하라면
    if len(lst)>0 and sum(ans) + lst[0] <= l:
        # 트럭이 다리에 올라간다
        now = lst[0]
        del lst[0]
    # 남은 트럭이 없거나 다음 트럭이 오면 다리가 견딜 수 있는 하중을 초과한다면
    else:
        # 다리에 올라가는 트럭은 없다
        now = 0
    ans.append(now)
    # 남은 트럭도 없고 다리 위에도 트럭이 없다면 반복문 종료
    if len(lst)==0 and sum(ans)==0:
        break
print(cnt)