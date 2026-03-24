N, X = map(int, input().split())
visits = [int(x) for x in input().split()]

max_sum = sum(visits[:X])
cur_sum = max_sum
cnt = 1
print(max_sum)
for i in range(N - X):
    cur_sum += visits[i + X] - visits[i]
    if cur_sum == max_sum:
        cnt += 1
    elif max_sum < cur_sum:
        max_sum = cur_sum
        cnt = 1
if max_sum:
    print(max_sum)
    print(cnt)
else:
    print("SAD")

# 5 2
# 1 4 2 5 1