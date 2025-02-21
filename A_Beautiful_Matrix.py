matrix =[[0 for i in range(5)] for i in range(5)]
for i in range(5):
    row = list(map(int,input().split()))
    matrix[i] = row

i,j =0,0
for r in range(5):
    for c in range(5):
        if matrix[r][c] ==1:
            i,j = r,c

moves = abs(j-2) + abs(i-2)
print(moves)