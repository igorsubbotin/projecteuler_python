# Project Euler #7: 10001st prime
p = [2, 3, 5]

def find_prime(n):
    global p
    i = p[len(p)-1]
    while True:
        if len(p) >= n:
            return p[n-1]
        i += 1
        found = True
        for j in p:
            if i % j == 0:
                found = False
                break
        if found:
            p.append(i)

t = int(raw_input())
for _ in xrange(t):
    n = int(raw_input())
    print find_prime(n)