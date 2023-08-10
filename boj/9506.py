while True:
    n = int(input())
    if n == -1:
        break
    else:
        cnt = 0
        a = [0]*n
        for j in range(2,n+1):
            if n % j == 0:
                a[cnt] = j
                cnt += 1
            if j == n-1:
                if sum(a)+1 == n:
                    print("{} = 1".format(n), end = "")
                    for k in a :
                        if k!=0:
                            print(" + {}".format(k), end = "")
                    print("")
                else:
                    print("{} is NOT perfect.".format(n))
                
