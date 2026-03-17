n, t = input().split()
n = int(n)
players = set()
game_types = {'Y': 1, 'F' : 2, 'O': 3}
for _ in range(n):
    players.add(input())

ans = len(players) // game_types[t]
print(ans)
