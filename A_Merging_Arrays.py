n, m = list(map(int,input().split()))
arr1 = list(map(int,input().split()))
arr2 = list(map(int,input().split()))

i,j =0,0
ans =[]
while i<n and j<m:
    if arr1[i]<=arr2[j]:
        ans.append(arr1[i])
        i +=1
    else:
        ans.append(arr2[j])
        j +=1
    
while i<n:
    ans.append(arr1[i])
    i +=1
while j <m:
    ans.append(arr2[j])
    j +=1
    

print(*ans)
