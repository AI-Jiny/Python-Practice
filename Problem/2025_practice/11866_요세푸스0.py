n, k = [int(x) for x in input().split()]
people_list = list(range(1, n + 1))
ordered_list = []
idx = 0

for _ in range(n):
    idx = (idx + k - 1) % len(people_list)
    ordered_list.append(str(people_list.pop(idx)))

answer = "<" + ", ".join(ordered_list) + ">"
print(answer)
