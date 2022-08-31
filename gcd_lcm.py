# def Swap(n, m):
#     return (m, n)

# based on Eucledian algorithm
# when n >m, n = m*q + r, then m become n & r becomes m until r is 0


def FindGcd(n, m):
    if (n % m) == 0:
        return m
    if (n < m):
        n, m = m , n
    while (m > 0):
        n , m = m, n % m
    return n

def FindLcm(n,m):
    large = max(n,m)
    small = min (n,m)
    i = large
    while(1):
        if(i%small == 0):
            return i
        i += large
    



n = int(input("Enter first number:"))
m = int(input("Enter second number:"))

gcd = FindGcd(n,m)
lcm = FindLcm(n,m)
#lcm = (n*m)/gcd

print("GCD of %d and %d is %d" %(n,m,gcd))
print("LCM of %d and %d is %d" %(n,m,lcm))

