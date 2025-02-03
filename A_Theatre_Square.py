dimension = list(map(int,input().split()))

m , n, a = dimension
vertical = int(m/a) if (m/a) == int(m/a) else ((m//a) +1)
horizontal = int(n/a) if (n/a) == int(n/a) else ((n//a) +1)

print(horizontal+vertical)
