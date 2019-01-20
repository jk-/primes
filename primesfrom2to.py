#!/usr/bin/env python2

import numpy as np

# n/3 + (n%6==2) = mod 24
# 24/3 = 8
# 24 mod 6 = 8

# 120/3 = 40
# 120 mod 6 = 0

# int(n**0.5)/3+1 n^0.5/3+1

#k=3*i+1|1 # | is binary bit OR

def primesfrom2to(n):
    sieve = np.ones(n/3 + (n%6==2), dtype=np.bool_) // 120 = 40
    sieve[0] = False
    for i in xrange(int(n**0.5)/3+1):
        if sieve[i]:
            k=3*i+1|1 # binary bit OR
            sieve[      ((k*k)/3)      ::2*k] = False
            sieve[(k*k+4*k-2*k*(i&1))/3::2*k] = False
    return np.r_[2,3,((3*np.nonzero(sieve)[0]+1)|1)]

primes = primesfrom2to(int(100000))

with open('primes_sieve.txt', 'w') as f:
    for item in primes:
        f.write("%s\n" % item)
