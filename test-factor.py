#!/usr/bin/env python3
from decimal import *
import math
import numpy as np
import time

key = Decimal(24989510334168154861762840052517131239617184454367090420756683371018854393048134881803782509924673236635848481726949
)


# loge(n) / loge(2)
# ln(n) / ln(2)


"""
usePrec = 60000

with localcontext() as ctx:
    ctx.prec = usePrec

    with open("a.txt") as f:
        n = [line.rstrip(" \n") for line in f]

    with open("factor.txt") as f:
        f = [line.rstrip(" \n") for line in f]

    print(Decimal("".join(n)) / Decimal("".join(f)))
"""
