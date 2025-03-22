from collections import defaultdict

t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    
    need = defaultdict(int)
    max_moves = 0
    
    for num in a:
        remainder = num % k
        if remainder != 0:
            add = k - remainder
            need[add] += 1
            max_moves = max(max_moves, add + (need[add] - 1) * k)
    
    print(max_moves + 1 if max_moves > 0 else 0)
