

n,x0 = map(int,input().split())

left =0
right =1000
for _ in range(n):
    a, b = map(int,input().split())
    left = max(left,min(a,b))
    right = min(right,max(a,b))

if left > right:
    print(-1)
else:
    if x0<left:
        print(left-x0)
    elif x0>right:
        print(x0-right)
    else:
        print(0)