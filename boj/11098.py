n = int(input())

for i in range(n):
    p = int(input())
    price = 0
    namelst = ""
    for j in range(p):
        c, name = input().split(" ")
        c = int(c)
        if c > price:
            price = c
            namelst = name
    print(namelst)
        
