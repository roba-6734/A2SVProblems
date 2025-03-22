t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    
    answer = "NO"
    
    
    for len_val in range(1, n):
       
        prefix = sorted(arr[:len_val])
        prefix_max = prefix[-1]
        
        
        suffix = sorted(arr[len_val:])
        suffix_min = suffix[0]
        
        
        if prefix_max > suffix_min:
            answer = "YES"
            break
    
    print(answer)