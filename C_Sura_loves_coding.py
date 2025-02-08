length = int(input())
result =[]
word = input()
i =0
for i in range(length-1,-1,-1):
    result.insert(len(result)//2,word[i])
ans = "".join(result)
print(ans)