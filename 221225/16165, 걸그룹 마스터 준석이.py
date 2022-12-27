N, M = map(int, input().split())
team_mem, mem_team = {}, {}
for i in range(N):
    team_name = input()
    num = int(input())
    team_mem[team_name] = []
    for j in range(num):
        name = input()
        team_mem[team_name].append(name)
        mem_team[name] = team_name
for i in range(M):
    name = input()
    num = int(input())
    if num == 0:
        for mem in sorted(team_mem[name]):
            print(mem)
    else:
        print(mem_team[name])