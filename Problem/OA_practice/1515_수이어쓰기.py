n_string = input()
cur_num = 0
for n in n_string:
    num = int(n)
    is_first = True
    while True:        
        if n in str(cur_num) and not is_first:
            break
        is_first = False
        cur_num += 1
    print(n, cur_num)


# 82340329923
# 43
# 00000000000000000000000000000000000000000000000000000000000000000000000
# 400
# 345029834023049820394802334909240982039842039483294792934790209
# 279and n != str(cur_num)[-1]