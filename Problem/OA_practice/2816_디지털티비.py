n = int(input())
channels = []
ans = ""
for _ in range(n):
    channels.append(input())

for i, target in enumerate(["KBS1", "KBS2"]):
    idx = channels.index(target) - i
    if idx:
        ans += "3" * (idx)
    if 1 < idx:
        ans += "2" + "4" * (idx - 1)
    if not i and "KBS2" not in [channels[0], channels[1]] and idx != 1:
        ans += "1"

print(ans)
