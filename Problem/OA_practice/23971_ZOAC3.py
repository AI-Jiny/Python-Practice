h, w, n, m = map(int, input().split())

max_col = (h + n) // (n + 1)
max_row = (w + m) // (m + 1)

print(max_col * max_row)

