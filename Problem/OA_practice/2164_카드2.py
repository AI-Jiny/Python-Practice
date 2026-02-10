n = int(input())
card = [i for i in range(1, n + 1)]

while len(card) > 1:
    card = card[1::2] if len(card) % 2 == 0 else (card[3::2]+card[1:2])
print(card[0])

# 1234567
345672
56724
7246
462

26
6