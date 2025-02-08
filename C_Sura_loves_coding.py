length = int(input())
result =[]
word = input()

for i in range(length-1,-1,-1):
    
    result.insert(len(result)//2,word[i])
    print(result)
ans = "".join(result)
print(ans)