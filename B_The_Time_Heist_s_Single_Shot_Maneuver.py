t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = int(input())

    prev = -float('inf')
    possible = True
    
    for num in a:
        
        original = num
        transformed = b - num
        
        
        if original >= prev and transformed >= prev:      
            prev = min(original, transformed)
        elif original >= prev:
            prev = original
        elif transformed >= prev:
            prev = transformed
        else:
            possible = False
            break
    
    print("YES" if possible else "NO")
