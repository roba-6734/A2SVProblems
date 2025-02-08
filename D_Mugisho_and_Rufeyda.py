n,t = list(map(int,input().split()))

lowest_possible = 10**(n-1)
upmost_possible = 10**n -1

if lowest_possible %t ==0:
    print(lowest_possible)
else:
    ans = lowest_possible + (t - lowest_possible%t)
    if ans <=upmost_possible:
        print(ans)
    else:
        print(-1)
