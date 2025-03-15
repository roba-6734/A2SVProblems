t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    count = 0
    i = 0
    
    while i < n:  
        l = i
        while i + 1 < n and a[i] == a[i + 1]:
            i += 1
        r = i
        left_ok = (l == 0 or a[l - 1] > a[l])
        right_ok = (r == n - 1 or a[r] < a[r + 1])
        
        if left_ok and right_ok:
            count += 1     
        i += 1
    
    print("YES" if count == 1 else "NO")