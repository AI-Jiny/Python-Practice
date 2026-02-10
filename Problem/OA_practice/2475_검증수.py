origin_input = input()
sum_numbers = sum(int(x)**2 for x in origin_input.split())
answer = sum_numbers % 10
print(answer)
