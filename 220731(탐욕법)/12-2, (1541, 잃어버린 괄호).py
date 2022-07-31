prob = list(input().split('-'))

for i in range(len(prob)):
    if i==0:
        answer = sum(map(int, prob[i].split('+')))
    else:
        now = sum(map(int, prob[i].split('+')))
        answer -= now
print(answer)