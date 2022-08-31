def Swap(n, m):
    return (m, n)

# based on Eucledian algorithm
# when n >m, n = m*q + r, then m become n & r becomes m until r is 0


def FindGcd(n, m):
    if (n % m) == 0:
        return m
    if (n < m):
        (n, m) = Swap(n, m)
    while (m > 0):
        n = n % m
        (n, m) = Swap(n, m)
    return n


n = int(input("Enter first number:"))
m = int(input("Enter second number:"))

print(FindGcd(n, m))
