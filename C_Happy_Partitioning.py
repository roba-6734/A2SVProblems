import math
rounds = int(input())
for _ in range(rounds):
    n = int(input())
    arr = list(map(int,input()))
    
    best = n
    mindiff = n
    total1 = sum(arr)
    total0 = n-total1
    left1 = 0
    left0 =0

    right1 = total1
    right0 = total0

   
    
    for i in range(n+1): 
        left = math.ceil(i/2)
        right = math.ceil((n-i)/2)

        if (left0 >= left )and (right1 >=right):
            diff = abs(n/2 -i)
            if diff <mindiff:
                mindiff = diff
                best = i
            elif diff == mindiff:
                best = min(best,i)

        if i<n:
            if arr[i] ==0:
                left0 +=1
                right0 -=1
            else:
                left1 +=1
                right1 -=1
        
            
        
    print(best)

    


