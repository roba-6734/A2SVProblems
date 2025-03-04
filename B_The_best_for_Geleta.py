rounds = int(input())
for _ in range(rounds):
    n,m = list(map(int,input().split()))
    arr = list(map(int,input().split()))
    current_max = max(arr)
    answer =[]

    for _ in range(m):
      
        sign,l,r = list(input().split())
        l = int(l)
        r = int(r)
        for i in range(n):
            if l <= arr[i] <=r:
                arr[i] += 1 if sign =="+" else -1
        
        answer.append(max(arr))

    
    print(*answer)
   
            
        
       
    
~~