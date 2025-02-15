passwd = input()
rounds = int(input())
words =[]


for _ in range(rounds):
    word = input().strip()
    words.append(word)

if passwd in words:
    print("YES")
    exit()

    

for w1 in words:
    for w2 in words:
       if passwd in  (w1+w2):
            print("YES")
            exit()
    

print("NO")


        





