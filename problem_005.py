# Project Euler #5: Smallest multiple
t = int(raw_input())

def find_min(n):
    i = 1
    while True:
        found = True
        for j in xrange(2, n+1):
            if i % j != 0:
                found = False
                break
        if found:
            return i
        i += 1

for _ in xrange(t):
    n = int(raw_input())
    print find_min(n)