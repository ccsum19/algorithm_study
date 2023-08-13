a, b = map(int, input().split())

#최대 공약수 구하기
def gcd(x, y):
    while y > 0:
        x, y = y, x % y
    return x

#최소 공배수 구하기
def lcm(x, y):
    return x * y / gcd(x, y)

print(int(gcd(a, b)))
print(int(lcm(a, b)))