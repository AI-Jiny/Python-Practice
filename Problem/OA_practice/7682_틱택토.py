ans = []

def check_winner(board, player):
    is_win = False

    win_case = [
        [0,1,2], [3,4,5], [6,7,8],
        [0,3,6], [1,4,7], [2,5,8],
        [0,4,8], [2,4,6]
    ]
    for c in win_case:
        if player == board[c[0]] == board[c[1]] == board[c[2]]:
            is_win = True
    return is_win

while True:
    b = input()
    if b == "end":
        break

    xo = {'X':0, 'O':0, '.': 0}

    for s in b:
        xo[s] += 1
    
    xwin = check_winner(b, 'X')
    owin = check_winner(b, 'O')

    if not (xo['X'] == xo['O'] or xo['X'] == xo['O'] + 1):
        ans.append("invalid")
    elif xwin and owin:
        ans.append("invalid")
    elif xwin and xo['O'] + 1 != xo['X']:
        ans.append("invalid")
    elif owin and xo['O'] != xo['X']:
        ans.append("invalid")
    elif not xwin and not owin and xo['.']:
        ans.append("invalid")
    else:
        ans.append("valid")

for an in ans:
    print(an)

