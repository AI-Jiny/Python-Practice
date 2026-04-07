import sys

input = sys.stdin.readline
s = input().rstrip()
n = int(input())
left_stack = list(s)
right_stack =[]

for _ in range(n):
    print(left_stack)
    print(right_stack)
    command, *value = input().split()
    if command == "L" and left_stack:
        right_stack.append(left_stack.pop())
    if command == "D" and right_stack:
        left_stack.append(right_stack.pop())
    if command == "B" and left_stack:
        left_stack.pop()
    if command == "P":
        left_stack.append(value[0])

ans = "".join(left_stack) + "".join(right_stack[::-1])
print(ans)

# abcd
# 3
# P x
# L
# P y