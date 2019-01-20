#!/usr/bin/env python3

from decimal import *
import math
import numpy as np
import time
import os.path

to_what_number = 1000000
end = math.floor(to_what_number/24+2)

i = 1
m = 24

f_name = 'potential-primes-1MM.npz'
last_p_on_hash = 1
use_hash = False
primes = [2,3]
file_exists = os.path.isfile(f_name)

if (file_exists and use_hash):
    data = np.load(f_name)
    last_p_on_hash = data['last_p_on_hash']
    primes = data['primeBusData']

pb = np.array([1,5,7,11,13,17,19,23])


def iteration(n, m):
    return (n//m)+1

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

t1_start = time.perf_counter()
t2_start = time.process_time()

while i < end:
    if (i % 500) == 0:
        t1_check = time.perf_counter()
        print("%d of %d (%d mins / %d)" % (i, end, (t1_check-t1_start)/60,t1_check-t1_start ))

    for b_idx, b in enumerate(pb):
        primes.append(getNominalNumberAtLoc(i, b, 1, m))
    i+=1

t1_stop = time.perf_counter()
t2_stop = time.process_time()

print("--------------------------------------------------")
print("Elapsed time: %.1f [min]" % ((t1_stop-t1_start)/60))
print("CPU process time: %.1f [min]" % ((t2_stop-t2_start)/60))
print("Found %d primes" % len(primes))
print("Outputting primes to disk and saving hash")

np.savez_compressed(f_name, primes=primes, last_p_on_hash=last_p_on_hash)

with open(f_name + '.txt', 'w') as f:
    for item in primes:
        f.write("%s\n" % item)

print("--------------------------------------------------")
