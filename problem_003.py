# Project Euler #3: Largest prime factor
def prime_factors(n):
    factors = []
    d = 2
    while n > 1:
        while n % d == 0:
            factors.append(d)
            n /= d
        d = d + 1
        if d*d > n:
            if n > 1: factors.append(n)
            break
    return factors

t = int(raw_input())

for _ in xrange(t):
    n = int(raw_input())
    pfs = prime_factors(n)
    print max(pfs)