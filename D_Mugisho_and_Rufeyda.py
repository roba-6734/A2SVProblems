n,t = list(map(int,input().split()))

lower_possible = 10**(n-1)
upper_possible = 10**n -1

if lower_possible %t ==0:
    print(lower_possible)
else:
    ans = lower_possible + (t - lower_possible%t)
    if ans <=upper_possible:
        print(ans)
    else:
        print(-1)
