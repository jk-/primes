#!/usr/bin/env python3

from decimal import *
import math
import numpy as np
import time

t1_start = time.perf_counter()
t2_start = time.process_time()

end = Decimal(23)

primes = []
primeBus = np.array([1,5,7,11,13,17,19,23])


# this is the interator on the nominal bus, goes to End
# goes from left to right
i = Decimal(5)

# this is the bus itterator, it goes through primeBus infinitely
# goe from top to bottom
b = 0

# this is the pointer for offseting primes, the sub bus
Sb = 0

'''
when we land on a prime we have to generate a few things

pb := {1,3,5,7,11,17,19,23}
n := number

psb := [pb * n] % 24
psbi := [pb * n] / 24 + 1

where pb is the prime bus
p is the current number
psb is the prime sub bus
psbi is the prime sub bus iteration, rounded down +1
'''

while i < end:
    if (i % 24) == 0:
        print(i)





t1_stop = time.perf_counter()
t2_stop = time.process_time()

print("--------------------------------------------------")
print("Elapsed time: %.1f [min]" % ((t1_stop-t1_start)/60))
print("CPU process time: %.1f [min]" % ((t2_stop-t2_start)/60))
print("Found %d primes" % len(primes))
print("Outputting primes to disk")

with open('primes.txt', 'w') as f:
    for item in primes:
        f.write("%s\n" % item)

print("--------------------------------------------------")
