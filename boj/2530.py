T = int(input(""))
R = 0
cnt = 0
while cnt < T:
    m = list(input("").split())
    R = float(m[0])
    for i in m:
        if i == "@":
            R = R * 3
        elif i == "%":
            R = R + 5
        elif i == "#":
            R = R - 7
    print('%.2f' %(R))
    cnt += 1
            
