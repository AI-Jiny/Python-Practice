N = int(input())
list_n = [int(n) for n in input().split()]
list_n.sort()
answer = 0

for i, n in enumerate(list_n):
    answer += n * (N - i)
print(answer)