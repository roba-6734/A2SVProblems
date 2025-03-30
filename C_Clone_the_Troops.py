t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    
    mod = 10**9 + 7
    
    
    max_subarray_sum = 0
    current_sum = 0
    
    for num in a:
        current_sum = max(0, current_sum + num)
        max_subarray_sum = max(max_subarray_sum, current_sum)
    
    
    original_sum = sum(a)
    
    
    if max_subarray_sum == 0:
      
        result = original_sum % mod
    else:
    
        power = pow(2, k, mod) - 1
        result = (original_sum + max_subarray_sum * power) % mod
    
    print(result)