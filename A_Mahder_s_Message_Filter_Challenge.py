t = int(input())
for _ in range(t):
    n = int(input())
    word = input()
    count =0
    for i in range(n-1,-1,-1):
        if word[i] ==')':
            count +=1
        else:
            break

    rest = n-count
    print("YES" if count > rest else"NO")