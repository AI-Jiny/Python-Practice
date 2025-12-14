N = int(input())
arr_n = [int(n) for n in input().split()]
M = int(input())
arr_m = [[int(m), i] for i, m in enumerate(input().split())]
arr_n.sort()
arr_m.sort()
arr_n.append(arr_n[-1])
answer_arr = [0] * M

idx_n = 0
for m, idx_m in  arr_m:
    while idx_n < N:
        if arr_n[idx_n] == m:
            answer_arr[idx_m] = 1
            break
        elif arr_n[idx_n] < m:
            if m < arr_n[idx_n + 1]:
                answer_arr[idx_m] = 0
                break
            else:
                idx_n += 1

        else:
            answer_arr[idx_m] = 0
            break

for a in answer_arr:
    print(a)