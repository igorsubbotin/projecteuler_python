# Project Euler #2: Even Fibonacci numbers
t = int(raw_input())

def fib_even(n):
    a = 1
    b = 2
    e = 0
    while True:
        t = a + b
        if b%2==0:
            e += b
        if t > n:
            return e
        a = b
        b = t
        
for _ in xrange(t):
    n = int(raw_input())
    f = fib_even(n)
    print f