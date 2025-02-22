rounds = int(input())
for _ in range(rounds):
    n = int(input())
    melody = list(map(int,input().split()))
    not_perfect = False
    for i in range(n-1):
        if abs(melody[i]-melody[i+1]) != 5 and abs(melody[i]-melody[i+1]) != 7:
            print("NO")
            not_perfect = True
            break
    if not not_perfect:
        print("YES")
    