T = int(input())
list_t = [[input() for x in range(3)] for y in range(T)]

for command, num, l in list_t:
    num = int(num)
    if num:
        l = l.strip("[]").split(",")
    else:
        l = []
    idx_left = 0
    idx_right = len(l) - 1
    arrow = 0
    is_flag = False

    for c in command:
        
        if c == "R":
            arrow = (arrow + 1) % 2
        elif c == "D":
            if idx_left <= idx_right:
                if arrow:
                    idx_right -= 1
                else:
                    idx_left += 1
            else:
                is_flag = True
                break
    
    if is_flag:
        print("error")
        continue

    if arrow:
        if idx_left >= 1:
            print(f"[{",".join(l[idx_right: idx_left -1: -1])}]")
            
        else:
            print(f"[{",".join(l[idx_right:: -1])}]")
            
    else:
        print(f"[{",".join(l[idx_left: idx_right + 1])}]")