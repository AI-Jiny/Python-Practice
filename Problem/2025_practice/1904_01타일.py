N = int(input())
list_n = [0] * N
list_n[0] = 1
if N > 1:
    list_n[1] = 2

for i in range(2, N):
    list_n[i] = (list_n[i - 1] + list_n[i - 2]) % 15746

print(list_n[N -1])