strength,iteration = list(map(int,input().split()))
opps = []
for i in range(iteration):
    x,y = list(map(int,input().split()))
    opps.append((x,y))

opps.sort()
result =""
for x,y in opps:
    if x >= strength:
        result ="NO"
        break
    else:
        strength +=y
        result = "YES"
print(result)