N, K = map(int, input().split())
hps = input()
burgers = [1 if hp == "H" else 0 for hp in hps]
ans = 0

for i in range(N):
    if hps[i] == "H":
        continue
    for j in range(max(i - K, 0), min(i + K + 1, N)):
        if not burgers[j]:
            continue

        burgers[j] = 0
        ans += 1
        break

print(ans)
# 20 1
# HHPHPPHHPPHPPPHPHPHP