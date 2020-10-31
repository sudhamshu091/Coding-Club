def magical(n, a, b):
        mod = 10**9 + 7

        l = a / gcd(a, b) * b
        m = (l / a) + (l / b) - 1
        k = n//m
        o = int(n % m)

        if o == 0:
            return k * l % mod

        head = [a ,b]
        for i in range(o - 1):
            if head[0] <= head[1]:
                head[0] += a
            else:
                head[1] += b

        return (k * l + min(head)) % mod
def gcd(x,y):
    a = max([x,y])
    b = min([x,y])
    if b == 0:
        return a
    else:
        return gcd(b,(a % b))
print(magical(4,2,3))
print(magical(1,2,3))
print(magical(5,2,4))
print(magical(3,6,4))
