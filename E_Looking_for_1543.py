def clockwise(mat,n,m):
    result =[]
    t,l = 0,0
    b,r = n-1,m-1
    while t <=b and l <=r:
        for i in range(l,r+1):
            result.append(mat[t][i])
        t +=1

        for i in range(t,b+1):
            result.append(mat[i][r])

        r -=1

        if t <= b:
            for i in range(r,l-1,-1):
                result.append(mat[b][i])
            b -=1
        if l <= r:
            for i in range(b,t-1,-1):
                result.append(mat[i][l])
            l +=1

        return "".join(result)

def count(trav,target ="1543"):
    return trav.count(target)

def solve():
    T = int(input())
    results =[]

    for _ in range(T):
        n,m = map(int,input().split())
        mat = [input().strip() for _ in range(n)]
        trav = clockwise(mat,n,m)
        results.append(str(count(trav)))
    
    print("\n".join(results))

