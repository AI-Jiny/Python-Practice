from collections import Counter
s = input()
counter = Counter(s)
zero = counter['0'] // 2
one = counter['1'] // 2

s = "".join(s.rsplit("0", zero))
s = "".join(s.split("1", one))
print(s)

