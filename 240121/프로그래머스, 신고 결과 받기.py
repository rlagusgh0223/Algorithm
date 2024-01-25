# 모범답안
def solution(id_list, report, k):
    # 신고한 사람이 받은 정지 메일 횟수를 저장할 리스트
    answer = [0] * len(id_list)
    # 신고 받은 횟수를 저장할 딕셔너리
    check = {x:0 for x in id_list}

    # set을 이용하여 유저 중복 신고를 제거한다
    for r in set(report):
        # r.split()으로 신고자, 신고당한자로 나뉘는데
        # 신고 당한사람의 신고 횟수를 증가시킨다
        check[r.split()[1]] += 1
    
    for r in set(report):
        # 신고 당한 사람의 신고 횟수가 k를 넘으면
        if check[r.split()[1]] >= k:
            # 신고한 사람에게 메일을 발송한다
            answer[id_list.index(r.split()[0])] += 1
    
    return answer


# def solution(id_list, report, k):
#     answer = {now:0 for now in id_list}
#     stop = []
#     report = [r.split() for r in report]
#     check = {now:0 for now in id_list}
#     human = {now:[] for now in id_list}
#     for r, p in report:
#         if p not in human[r]:
#             human[r].append(p)
#             check[p] += 1
#     for cr, cp in check.items():
#         if cp >= k:
#             stop.append(cr)
#     for hr, hp in human.items():
#         for s in stop:
#             if s in hp:
#                 answer[hr] += 1
#     return list(answer.values())





import sys
id_list = list(sys.stdin.readline().strip().split('", "'))
report = list(sys.stdin.readline().strip().split('", "'))
k = int(sys.stdin.readline())
print(solution(id_list, report, k))