num_questions = int(input())
count =0
for i in range(num_questions):
    confidence = list(map(int,input().split()))
    if sum(confidence) >=2:
        count +=1
print(count)
