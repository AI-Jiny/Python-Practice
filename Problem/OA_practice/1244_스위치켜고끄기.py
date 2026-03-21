N = int(input())
switches = [0] + [int(x) for x in input().split()]
M = int(input())
students = []
for _ in range(M):
    stu_s, stu_n = map(int, input().split())
    students.append((stu_s, stu_n))

for s, n in students:
    if s == 1:
        idx = n
        while idx <= N:
            switches[idx] ^= 1
            idx += n
    if s == 2:
        gap = 0
        while n + gap <= N and gap < n and switches[n - gap] == switches[n + gap]:
            gap += 1
        gap -= 1

        for i in range(n - gap, n + gap + 1):
            switches[i] ^= 1
switches = [str(x) for x in switches]
idx = 1
while idx <= N:
    print(" ".join(switches[idx: idx+20]))
    idx += 20