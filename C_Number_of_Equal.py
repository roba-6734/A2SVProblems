n, m = map(int, input().split())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

count = 0
i = 0
j = 0

while i < n and j < m:
    if arr1[i] == arr2[j]:
        
        curr_val = arr1[i]
        count_a = 0
        count_b = 0
        
        
        while i < n and arr1[i] == curr_val:
            count_a += 1
            i += 1
            
       
        while j < m and arr2[j] == curr_val:
            count_b += 1
            j += 1
            
        
        count += count_a * count_b
    elif arr1[i] < arr2[j]:
        i += 1
    else:  
        j += 1

print(count)