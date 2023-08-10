dish = input()
cnt = len(dish)
h = 10
    
for i in range(1,cnt):  

    if dish[i] == "(":
        if dish[i-1] == "(":
            h += 5
        else:
            h += 10
    else:
        if dish[i-1] == ")":
            h+= 5
        else: h += 10

print(h)
