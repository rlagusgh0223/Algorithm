import sys
y1, m1, d1 = map(int, sys.stdin.readline().split())
y2, m2, d2 = map(int, sys.stdin.readline().split())
if m1 < m2:  # 연도가 적을일은 없고 월이 더 크다면 연도만 계산하면 된다
    year1 = y2 - y1
elif m1==m2 and d1<=d2:  # 월이 같아도 날짜가 더 앞서면 계산에 지장 없다
    year1 = y2 - y1
else:
    year1 = y2 - y1 - 1  # 월이 더 작거나 일이 더 작다면 아직 완전한 1년이 지난건 아니므로 1살을 더 빼줘야 된다
year2 = y2 - y1 + 1
year3 = y2 - y1
print(year1)
print(year2)
print(year3)