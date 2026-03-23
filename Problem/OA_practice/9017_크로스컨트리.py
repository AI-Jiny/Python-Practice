from collections import Counter

T = int(input())
ans = []
for _ in range(T):
    _ = input()
    rank = [int(x) for x in input().split()]
    team_counts = Counter(rank)
    teams = {}
    score = 1
    for r in rank:
        if team_counts[r] < 6:
            continue
        team = teams.get(r, [0])
        team.append(score + team[-1])
        teams[r] = team
        score += 1
    
    win_score = (10e6, 10e6, 10e6)
    for k,v in teams.items():
        s = (v[4], v[5], k)
        if s < win_score:
            win_score = s
    ans.append(win_score[2])

for an in ans:
    print(an)

# # 2
# # 15
# # 1 2 3 3 1 3 2 4 1 1 3 1 3 3 1
# # 18
# # 1 2 3 1 2 3 1 2 3 3 3 3 2 2 2 1 1 1
