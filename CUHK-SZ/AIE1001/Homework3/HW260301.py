def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

values = input().split()
a = int(values[0])
b = int(values[1])
print(gcd(a, b))