t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    
    
    cache = {}
    
    def max_coins(left, right):
        
        if left > right:
            return 0
            
        
        if (left, right) in cache:
            return cache[(left, right)]
        
        max_value = 0
        
        
        for i in range(left, right + 1):
            current_value = abs(a[i])
            
            
            if a[i] < 0:  
                next_value = max_coins(left, i - 1)
            else:  
                next_value = max_coins(i + 1, right)
                
            max_value = max(max_value, current_value + next_value)
        
        cache[(left, right)] = max_value
        return max_value
    
    print( max_coins(0, n - 1))


    