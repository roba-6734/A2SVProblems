test_cases = int(input())
for i in range(test_cases):
    n = int(input())
    count  =0
    elements = list(map(int,input().split()))
    for i in range(n):
        for j in range(i+1,n):
            if elements[j]-elements[i] == j-i:
                count +=1
    print(count)
