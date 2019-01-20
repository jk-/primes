#!/usr/bin/env python3

from decimal import *
import math
import numpy as np
import time

t1_start = time.perf_counter()
t2_start = time.process_time()

pi = Decimal(math.pi)
pi2 = 2 * pi

# Populate array from 2 to 359
d = np.arange(Decimal(2),Decimal(360))

usePrec = 1335

with localcontext() as ctx:
    ctx.prec = usePrec
    ctx.Emax = 99999999

    with open("a.txt") as f:
        n = [line.rstrip(" \n") for line in f]

    n = Decimal("".join(n))
    print("n created")

    k = pi2 / Decimal(n)
    print("k found")

    dR = k * 180 / pi
    print("dR found")

    # Convert the array to degrees in radians
    d[:] = [ (pi2 / Decimal(x)) * (180 / pi) for x in d]

    # Divide the degrees in a circle by the the degrees in N
    d[:] = [Decimal(x) / Decimal(dR) for x in d]
    print("d division complete")

    convex = np.copy(d)

    # Determine if the number is prime by convergence of degrees
    d[:] = [Decimal(x) - Decimal(x).quantize(Decimal('1.')) for x in d]

    print("d stripped for prime")

# get the factor indexes
fIndexes = np.where(d == 0)[0]

factors = [convex[i] for i in fIndexes]

t1_stop = time.perf_counter()
t2_stop = time.process_time()

print("--------------------------------------------------")
if (len(fIndexes) == 0):
    print ("That number is Prime!")
else:
    print ("Not Prime!")
    print (factors)
print("--------------------------------------------------")

print("Elapsed time: %.1f [min]" % ((t1_stop-t1_start)/60))
print("CPU process time: %.1f [min]" % ((t2_stop-t2_start)/60))
print("--------------------------------------------------")
