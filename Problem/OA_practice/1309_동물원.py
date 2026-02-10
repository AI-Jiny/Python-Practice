N = int(input())
list_n = [0] * (N + 1)
list_n[0] = 1
list_n[1] = 3

for i in range(2, N + 1):
    list_n[i] = (2 * list_n[i - 1] + list_n[i - 2]) % 9901

print(list_n[N])