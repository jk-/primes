#!/usr/bin/env python3

from decimal import *
import math
import numpy as np
import time
import os.path

for i in range(25):
    print((i*24)//24+1)

'''
    Theory is that
    if n%24 on mod bus
        and (n//24+1)%24 is on mod bus


    n is prime

def iteration(n, m):
    return (n//m)+1

i = 1
m = 24
to_what_number = 120

primes = []

pb = np.array([1,5,7,11,13,17,19,23])

t1_start = time.perf_counter()
t2_start = time.process_time()

while i <= to_what_number:
    if i%m in pb:
        r = iteration(i,m)%24
        while r > 25:
            r = iteration(i,m)
            if r in pb:
                primes.append(i)
                break

    i+=1

f_name = 'p-test.txt'

t1_stop = time.perf_counter()
t2_stop = time.process_time()

print("--------------------------------------------------")
print("Elapsed time: %.1f [min]" % ((t1_stop-t1_start)/60))
print("CPU process time: %.1f [min]" % ((t2_stop-t2_start)/60))
print("Found %d primes" % len(primes))
print("Outputting primes to disk")

with open(f_name, 'w') as f:
    for item in primes:
        f.write("%s\n" % item)

print("--------------------------------------------------")

'''
