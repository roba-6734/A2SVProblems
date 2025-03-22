q = int(input())

for _ in range(q):
    n, k = map(int, input().split())
    s = input()
    
    min_changes = float('inf')
    
    pattern1 = "RGB" * (n // 3 + 1)
    pattern2 = "GBR" * (n // 3 + 1)
    pattern3 = "BRG" * (n // 3 + 1)
    
    for pattern in [pattern1, pattern2, pattern3]:
        changes = sum(1 for i in range(k) if s[i] != pattern[i])
        min_changes = min(min_changes, changes)
        
        for i in range(k, n):
            if s[i] != pattern[i]:
                changes += 1
            if s[i - k] != pattern[i - k]:
                changes -= 1
            min_changes = min(min_changes, changes)
    
    print(min_changes)
