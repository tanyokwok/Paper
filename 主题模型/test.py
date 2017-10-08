#encoding=utf-8
#########################################################################
# File Name: test.py
# Author: GuoTianyou
# mail: fortianyou@gmail.com
# Created Time: 六  4/22 11:40:28 2017
#########################################################################

import matplotlib.pyplot as plt
import random as rand

x = [rand.randint(0, 10) for v in range(0, 1000)]

p = 0.05
b1 = 5
b2 = 5 / p

for i in range(0, 1000):
    b1 = b1 * (1 - p) + p * x[i]
    b2 = b2 * (1 - p) + x[i]
    b3 = b2 * p
    print str(b1) + " " + str(b2) + " " + str(b3)
