word = input()
alpha = {}
alpha_re = {}

for w in word:
    w = w.upper()
    cnt = alpha.get(w, 0)
    alpha[w] = cnt + 1

for k, v in alpha.items():
    l = alpha_re.get(v , [])
    l.append(k)
    alpha_re[v] = l

ma = max(alpha_re.keys())
if len(alpha_re[ma]) > 1:
    print("?")
else:
    print(alpha_re[ma][0])