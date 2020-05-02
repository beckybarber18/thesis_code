#https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.rv_continuous.html 

import scipy.stats as st
from statistics import *
import matplotlib.pyplot as plt
from random import *

def draw_val():
	q = random()
	return 1/(1-q)

samples = []
num_samples = 10000
for i in range(num_samples):
	samples.append(draw_val())
	if i % 1000 == 0: print('i:', i)

print('mean:', mean(samples))
num_bins = 2000
plt.hist(samples, num_bins)
plt.xlim(0,150)
plt.show()
