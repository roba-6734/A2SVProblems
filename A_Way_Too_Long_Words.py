iteration = int(input())
for i in range(iteration ):
    word = input()
    if len(word)<=10:
        print(word)
    else:
        middle_chars = len(word)-2
        print(word[0],middle_chars,word[-1],sep="")