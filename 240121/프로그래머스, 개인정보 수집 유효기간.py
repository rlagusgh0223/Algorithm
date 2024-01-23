def solution(today, terms, privacies):
    answer = []
    # 유효기간을 계산할 수 있도록 연, 월, 일 별로 숫자로 바꾼다
    today = list(map(int, today.split(".")))

    check = {}
    # 각각의 단계에 맞는 유효기간을 일수로 맞춘다
    # ex) 6달 = 6*28일(모든 달은 28일이라고 문제에서 주어졌다)
    for term in terms:
        ck, day = term.split()
        check[ck] = int(day) * 28
    
    # 각 개인정보를
    for i in range(len(privacies)):
        # 개인정보 수집 날짜와 약관 별로 나눈다
        date, ck = privacies[i].split()
        # 개인정보 수집 날짜는 숫자로 바꾼 후 유효기간 연, 월, 일과 비교 후
        # 일수로 바꿔 개인정보 수집일로부터 며칠이 지났는지 계산한다
        date = list(map(int, date.split(".")))
        year = (today[0] - date[0]) * 12 * 28
        month = (today[1] - date[1]) * 28
        day = today[2] - date[2]
        total = year + month + day
        # 유효기간은 보관가능한 일자를 나타내므로 그 값보다 작은게 아니라면 보관 기간이 지난거다
        # 입력한 날짜도 1일이므로 3달 유효기간인 84일은 0~83일까지가 보관기간인거다
        if check[ck] <= total:
            answer.append(i+1)
    return answer


import sys
today = sys.stdin.readline().strip()
terms = list(sys.stdin.readline().strip().split('", "'))
privacies = list(sys.stdin.readline().strip().split('", "'))
print(solution(today, terms, privacies))