T = int(input())
ans = []
for _ in range(T):
    n, k, t, m = map(int, input().split())
    board = {}
    for c in range(m):
        i, j, s = map(int, input().split())
        team_score = board.get(i, [{}, 0, 0])
        score = team_score[0].get(j, 0)
        if score < s:
            team_score[0][j] = s
        team_score[1] += 1
        team_score[2] = c
        board[i] = team_score
    
    ranking = list(board.keys())
    ranking.sort(key=lambda x: (sum(board[x][0].values()), -board[x][1], -board[x][2]), reverse=True)

    ans.append(ranking.index(t) + 1)
for an in ans:
    print(an)
# 2
# 3 4 3 5
# 1 1 30
# 2 3 30
# 1 2 40
# 1 2 20
# 3 1 70
# 4 4 1 10
# 1 1 50
# 2 1 20
# 1 1 80
# 3 1 0
# 1 2 20
# 2 2 10
# 4 3 0
# 2 1 0
# 2 2 100
# 1 4 20