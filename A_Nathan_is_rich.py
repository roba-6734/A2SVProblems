round = int(input())
for i in range(round):
    value = int(input())
    ans = value //4 + (value%4)//2
    print(ans)