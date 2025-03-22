# t = int(input())
# for _ in range(t):
#     n = int(input())
#     p = list(map(int, input().split()))
    
#     beautiful = ['0'] * n
    
#     for l in range(n):
#         max_val = 0
#         seen = set()
        
#         for r in range(l, n):
#             current = p[r]
#             seen.add(current)
#             max_val = max(max_val, current)

#             if max_val == len(seen):
#                 beautiful[max_val - 1] = '1'
    
#     print(''.join(beautiful))

t = int(input().strip())

for _ in range(t):
    n = int(input().strip())
    p = list(map(int, input().split()))
    
    pos = [0] * n
    for i in range(n):
        pos[p[i] - 1] = i
    
    
    beautiful = ['0'] * n
    
    for m in range(1, n + 1):
        min_pos = min(pos[:m])
        max_pos = max(pos[:m])
        
        if max_pos - min_pos == m - 1:
            beautiful[m - 1] = '1'
    
    print(''.join(beautiful))
