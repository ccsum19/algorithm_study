while True:
    a, b = map(int, input().split(" "))
    if a == b == 0:
        break
    else:
        A = max(a, b)
        B = min(a, b)
        if A%B == 0:
            if(A == a):
                print("multiple")
            else:
                print("factor")
        else:
            print("neither")
            
