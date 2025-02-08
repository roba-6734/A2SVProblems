a = [11, 7, 1, 13, 21, 3, 7, 3]

b= [11, 3, 7, 1, 7]
a.sort()
b.sort()
print(a[:len(b)])
print(a[:len(b)] ==b)
