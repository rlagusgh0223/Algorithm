import sys
N = int(sys.stdin.readline())
d = {"A+": 4.3, "A0": 4.0, "A-": 3.7,
"B+": 3.3, "B0": 3.0, "B-": 2.7,
"C+": 2.3, "C0": 2.0, "C-": 1.7,
"D+": 1.3, "D0": 1.0, "D-": 0.7,
"F": 0.0}
cnt, ans = 0, 0
for i in range(N):
    sub, s, g = sys.stdin.readline().split()
    cnt += int(s)
    ans += d[g]*int(s)
print("{:.2f}".format(ans/cnt+0.00000000000001))  # 뒤에 0.0000~1 안 넣어주면 3.725를 3.27로 출력한다



# 딕셔너리를 이용하는게 더 좋은거 같다
# 시간과 메모리는 같지만 구현이 더 편하다
# import sys
# N = int(sys.stdin.readline())
# ans, cnt = 0, 0
# for i in range(N):
#     sub, score, grade = sys.stdin.readline().split()
#     if grade == 'A+':
#         cnt += int(score)
#         ans += int(score)*4.3
#     elif grade == 'A0':
#         cnt += int(score)
#         ans += int(score)*4.0
#     elif grade == 'A-':
#         cnt += int(score)
#         ans += int(score)*3.7
#     elif grade == 'B+':
#         cnt += int(score)
#         ans += int(score)*3.3
#     elif grade == 'B0':
#         cnt += int(score)
#         ans += int(score)*3.0
#     elif grade == 'B-':
#         cnt += int(score)
#         ans += int(score)*2.7
#     elif grade == 'C+':
#         cnt += int(score)
#         ans += int(score)*2.3
#     elif grade == 'C0':
#         cnt += int(score)
#         ans += int(score)*2.0
#     elif grade == 'C-':
#         cnt += int(score)
#         ans += int(score)*1.7
#     elif grade == 'D+':
#         cnt += int(score)
#         ans += int(score)*1.3
#     elif grade == 'D0':
#         cnt += int(score)
#         ans += int(score)*1.0
#     elif grade == 'D-':
#         cnt += int(score)
#         ans += int(score)*0.7
#     else:
#         cnt += int(score)
# print("{:.2f}".format(ans/cnt+0.0000000000001))