def check(key):
    for i in range(3):
        if key in keyboard[i]:
            return i, keyboard[i].index(key)


sl, sr = input().split()
zoac = list(input().strip())
cnt = 0

keyboard = ['qwertyuiop', 'asdfghjkl', 'zxcvbnm']

sl_row, sl_col,  = check(sl)
sr_row, sr_col,  = check(sr)

for z in zoac:
    row, col = check(z)

    if(row < 2 and col < 5) or (row == 2 and col < 4):
        cnt += abs(sl_row - row) + abs(sl_col - col) + 1
        sl_row, sl_col = row, col
    else:
        cnt += abs(sr_row - row) + abs(sr_col - col) + 1
        sr_row, sr_col = row, col

print(cnt)