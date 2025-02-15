from copy import deepcopy
n = int(input())
nums = list(map(int,input().split()))
ordered = [(nums[i],i+1) for i in range(n)]

ordered.sort()
answer =[]

for i in range(n//2):
    answer.append((ordered[i][1],ordered[n-i-1][1]))

for x,y in answer:
    print(x,y)

