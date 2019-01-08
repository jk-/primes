#!/usr/bin/env python3

#from decimal import *
import math
import numpy as np
import time
import os.path


to_what_number = 80
end = math.floor(to_what_number/24+2)

i = 1
m = 24

f_name = 'prime_bus.npz'
last_p_on_hash = 1
use_hash = False
primeBusData = []
primes = [1,2,3]
file_exists = os.path.isfile(f_name)

if (file_exists and use_hash):
    data = np.load(f_name)
    last_p_on_hash = data['last_p_on_hash']
    primeBusData = data['primeBusData']

pb = np.array([5,7,11,13,17,19,23])

def getNominalNumberAtLoc(i, b, d, m):
    return (b*d)+(((i-1)*m)*d)

def generatePrimeBus(n, m):
    pb_ones = np.array([1,1,1,1,1,1,1])
    psb = pb * n
    psb_nb = psb % m
    psb_ni = [math.floor(x/m+1) for x in psb]

    if (n == 1):
        psb_ni = pb_ones
    return np.array([psb_nb, psb_ni, psb])

def prime(n, b_idx, i):
    if n in pb and skip:
        return True

    # [ 1  5  7 11 13 17 19 23] [1 1 1 1 1 1 1 1]
    #print("%s: Converted %d nominal bus" % (n, pb[b_idx]))

    for p_idx, p in enumerate(primeBusData):
        n_i = math.floor(i/24+1)

        # current prime testing against
        ps_n = p[2][0]/p[2][0]

        if ps_n*2+1 > n:
            continue

        ps_n_i = p[1][b_idx]

        # this takes the nominal bus and converts it to sub bus row
        ps_cross_bus = p[0][b_idx]
        #print("%s: ...to sub prime bus %d for prime %d" % (n, ps_cross_bus, ps_n))

        ps_cross_i = math.floor(1+(n_i/ps_n))

        # grab the number to multiply
        #print("%d: ...taking nominal iteration of %d into %d, got %d" % (n,n_i,ps_n,ps_cross_i))

        # getting ready to find sub bus location
        ps_loc = math.floor(ps_n/24+1)+((ps_cross_i-1)*ps_n)

        #print("%d: ..loc invalid? (%d, %d, %d)" % (n, ps_loc, b, i))

        if (i == ps_loc):
            #print("...Invalidated %d with %d" % (n, ps_n))
            return False

    #print("Found prime %d" % n)
    return True

t1_start = time.perf_counter()
t2_start = time.process_time()

if len(primeBusData) == 0:
    while i < 2:
        for b_idx, b in enumerate(pb):
            # we are already mod 24 by forcing pb look-up
            n = getNominalNumberAtLoc(i, b, 1, m)
            n_i = math.floor(n/m+1)

            if n not in primes:
                primes.append(n)

            if (n > last_p_on_hash):
                primeBusData.append(generatePrimeBus(n,m))
                last_p_on_hash = n
        i+=1

primes.sort()

while i < end:

    if (i % 500) == 0:
        t1_check = time.perf_counter()
        print("%d of %d (%d mins)" % (i, end, (t1_check-t1_start)/60))

    for b_idx, b in enumerate(pb):
        # we are already mod 24 by forcing pb look-up
        n = getNominalNumberAtLoc(i, b, 1, m)
        n_i = math.floor(n/m+1)

        #print("Evaluating %d for primality at (%d, %d)" % (n, i, b))
        is_prime = prime(n, b_idx, i)

        if (is_prime and n not in primes):
            primes.append(n)

        if (n > last_p_on_hash):
            primeBusData.append(generatePrimeBus(n,m))
            last_p_on_hash = n
    i+=1

t1_stop = time.perf_counter()
t2_stop = time.process_time()

print("--------------------------------------------------")
print("Elapsed time: %.1f [min]" % ((t1_stop-t1_start)/60))
print("CPU process time: %.1f [min]" % ((t2_stop-t2_start)/60))
print("Found %d primes" % len(primes))
print("Outputting primes to disk and saving hash")

np.savez_compressed('prime_bus.npz', primeBusData=primeBusData, last_p_on_hash=last_p_on_hash)

with open('primes.txt', 'w') as f:
    for item in primes:
        f.write("%s\n" % item)

print("--------------------------------------------------")
