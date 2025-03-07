def solve():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    
    a.sort()
    
    if k == 0:
        if a[0] > 1:
            return a[0] - 1
        else:
            return -1
    
    if k == n:
        return a[n-1]
    
    if k < n and a[k-1] != a[k]:
        return a[k-1]
    else:
        return -1

print(solve())