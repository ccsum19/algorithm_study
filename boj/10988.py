a = list(str(input()))
n = len(a)
b = []
for i in range(n):
    b.append(a[n-i-1])

if a == b:
    print(1)
else:
    print(0)
