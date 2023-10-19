def algorithm_gcd(m, n):
    if n == 0:
        return m
    else:
        return algorithm_gcd(n, n % m)

m, n = int(input()), int(input())
print(algorithm_gcd(m,n))