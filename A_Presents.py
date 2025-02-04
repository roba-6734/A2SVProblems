friends = int(input())

gifts = list(map(int,input().split()))

people = [0]*friends
for i in range(len(gifts)):
    people[gifts[i]-1] = i+1

for num  in people:
    print(num, end=" ")





