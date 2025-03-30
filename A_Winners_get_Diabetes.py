t = int(input())
for _ in range(t):
    n  = int(input())
    s = list(input())
    seen = set()
    count =0
    for char in s:
        if char not in seen:
            count +=2
            seen.add(char)
        else:
            count +=1

    print(count)