iteration = int(input())
for i in range(iteration):
    a,b,c = list(map(int,input().split()))
    maximum =0
    for i in range (6):
        for j in range(6-i):
            for k in range(6-i-j):
                maximum = max(maximum,(a+i)*(b+j)*(c+k))
    print(maximum)

  
