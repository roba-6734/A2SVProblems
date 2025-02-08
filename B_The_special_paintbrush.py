iter = int(input())
for i in range(iter):
    lines = int(input())
    cells = input()
    b_count = cells.count("B")
    if b_count ==1:
        print(1)
    else:
        count = 0
        i,j =0,0
        for k in range(lines):
            if cells[k] =='B' and count ==0:
                i = k 
                count +=1
            elif cells[k] =='B' and count == b_count-1:
                j =k
                count +=1
                break
            elif cells[k] =='B':
                count +=1
            
        print(j-i+1)
        