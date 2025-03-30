t = int(input().strip())
enter = list(map(int, input().split()))
exit_order = list(map(int, input().split()))
exit_pos = [0] * (t + 1)
for i in range(t):
    exit_pos[exit_order[i]] = i
max_exit = -1
count = 0
for troop in enter:
    pos = exit_pos[troop]
    if pos > max_exit:
        max_exit = pos
    else:
        count += 1
print(count)
