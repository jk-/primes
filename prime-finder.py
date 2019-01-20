#!/usr/bin/env python3

from decimal import *
import math
import numpy as np
import time
import os.path

def iteration(n, m, addOne=True):
    return (n//m)+(1 if addOne else 0)

i = 1
m = 24

to_what_number = 10000
end = iteration(to_what_number,m)+1

f_name = 'prime_bus.npz'
last_p_on_hash = 1
use_hash = False
primeBusData = []
primes = [2,3]
file_exists = os.path.isfile(f_name)

pb = np.array([1,5,7,11,13,17,19,23])

if (file_exists and use_hash):
    data = np.load(f_name)
    last_p_on_hash = data['last_p_on_hash']
    primeBusData = data['primeBusData']

def getNominalNumberAtLoc(i, b, d, m):
    return (b*d)+(((i-1)*m)*d)

def generatePrimeBus(n, m):
    pb_ones = np.array([1,1,1,1,1,1,1,1])
    psb = pb * n
    psb_nb = psb % m
    psb_n = np.array([n,n,n,n,n,n,n,n])
    psb_ni = [iteration(x,m) for x in psb]

    if (n == 1):
        psb_ni = pb_ones
    return [psb_nb, psb_ni, psb, psb_n]

def prime(n, b_idx, i):
    if n in pb:
        return True

    # [ 1  5  7 11 13 17 19 23] [1 1 1 1 1 1 1 1]
    #print("%s: Converted %d nominal bus" % (n, pb[b_idx]))
    for x_idx, p in enumerate(primeBusData):

        n_i = iteration(n,m)
        bus = p

        #print(bus)
        # current prime testing against
        ps_n = math.floor(bus[3][0])

        if ps_n*2-1 > n:
            continue

        ps_n_i = bus[1][b_idx]

        # this takes the nominal bus and converts it to sub bus row
        ps_cross_bus = bus[0][b_idx]

        #print("%s: ...to sub prime bus %d for prime %d" % (n, ps_cross_bus, ps_n))
        #print("%s: ...n_i is %d iteration is %d" % (n, n_i, ps_n))


        ## nasty hack for rounding errors on 23
        ps_cross_i = iteration(n_i,ps_n)

        # grab the number to multiply
        #print("%d: ...taking nominal iteration of %d into %d, got %d" % (n,n_i,ps_n,ps_cross_i))

        addOne = True
        # getting ready to find sub bus location
        ps_cross_i_n = ((ps_cross_i-1)*ps_n)

        if ps_n == 1 and ps_cross_i >= m:
            addOne = False

        ps_loc = iteration(ps_n*ps_cross_bus,m, addOne=addOne)+ps_cross_i_n

        #math.floor((ps_n*ps_cross_bus)/24)+1+((ps_cross_i-1)*ps_n)

        #print("%d: ..loc invalid? (%d, %d, %d)" % (n, ps_loc, b, i))

        '''
        if n == 557:
            print("%s: ...to sub prime bus %d for sub prime %d" % (n, ps_cross_bus, ps_n))
            print("%s: ...n_i is %d and %d is sub prime iteration" % (n, n_i, ps_n_i))
            print("%d: ...taking nominal iteration of %d into %d, got %d (-1)" % (n,n_i,ps_n,ps_cross_i))
            print("%d: ..loc invalid? (%d, %d, %d)" % (n, ps_loc, b, i))
            print(bus[0])
            print(b_idx)
            print(ps_cross_bus)
            print(ps_n*ps_cross_bus)
            print(ps_cross_i-1)
            print(iteration(ps_n*ps_cross_bus,m, addOne=addOne))
            print((ps_cross_i-1)*ps_n)
            print(n_i,ps_n,ps_n_i,ps_cross_bus,ps_cross_i,ps_loc,ps_cross_i_n)
            print(i == ps_loc, i, ps_loc)
            quit()
        '''

        if (i == ps_loc):
            #print("...Invalidated %d with %d" % (n, ps_n))
            return False

    #print("Found prime %d" % n)
    return True

t1_start = time.perf_counter()
t2_start = time.process_time()

populate = 1
if len(primeBusData) == 0:
    while populate < 2:
        for b_idx, b in enumerate(pb):
            # we are already mod 24 by forcing pb look-up
            n = getNominalNumberAtLoc(populate, b, 1, m)

            if (n not in primes):
                primes.append(n)
                generatedData = generatePrimeBus(n,m)
                primeBusData.append(generatedData)
        populate+=1

primes.sort()

while i < end:

    if (i % 500) == 0:
        t1_check = time.perf_counter()
        print("%d of %d (%d mins / %d secs (total))" % (i, end, (t1_check-t1_start)/60, t1_check-t1_start ))

    for b_idx, b in enumerate(pb):
        # we are already mod 24 by forcing pb look-up
        n = getNominalNumberAtLoc(i, b, 1, m)

        #print("Evaluating %d for primality at (%d, %d)" % (n, i, b))
        is_prime = prime(n, b_idx, i)

        if (is_prime and n not in primes):
            primes.append(n)
            #print(primeBusData)
            generatedData = generatePrimeBus(n,m)
            primeBusData.append(generatedData)
            #print(primeBusData)
            last_p_on_hash = n
    i+=1

#print(primeBusData)
t1_stop = time.perf_counter()
t2_stop = time.process_time()

print("--------------------------------------------------")
print("Elapsed time: %.1f [min]" % ((t1_stop-t1_start)/60))
print("CPU process time: %.1f [min]" % ((t2_stop-t2_start)/60))
print("Found %d primes" % len(primes))
print("Outputting primes to disk and saving hash")

if (use_hash):
    np.savez_compressed(f_name, primeBusData=primeBusData, last_p_on_hash=last_p_on_hash)

with open('primes.txt', 'w') as f:
    for item in primes:
        f.write("%s\n" % item)

print("--------------------------------------------------")
