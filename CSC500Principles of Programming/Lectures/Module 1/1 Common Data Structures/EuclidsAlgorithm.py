# Find greatest common denominator of two numbers using EuclidsAlgorithm

def gcd(a, b):
    while (b != 0):
        temp = a
        a = b
        b = temp % b
    return a


print(gcd(60, 96)) # Should be 12
print(gcd(20, 8)) # Should be 4