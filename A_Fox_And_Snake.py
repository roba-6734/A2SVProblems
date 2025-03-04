r,c = list(map(int,input().split()))
end = True
for i in range(r):  
    if i %2 ==0:
        print("#"*c)
    elif end:
        print(("."*(c-1)) +"#")
        end = False
    else:
        print("#"+("."*(c-1)))
        end = True
