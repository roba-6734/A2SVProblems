size = int(input())
user_input = input()
count =0
for i in range(1,size):
    if user_input[i] == user_input[i-1]:
        count +=1
    
print(count)