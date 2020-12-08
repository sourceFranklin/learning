# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 06:51:59 2020

@author: franklin
"""

import numpy as np
import scipy.stats as si

combi = np.loadtxt('combi.csv', delimiter=',')

S = combi[:,0]
sigma = combi[:,1]

K, T, r = (100, 1, 0.05)

d1 = (np.log(S / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
d2 = (np.log(S / K) + (r - 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
result = (S * si.norm.cdf(d1, 0.0, 1.0) - K * np.exp(-r * T) * si.norm.cdf(d2, 0.0, 1.0))


"""
出力例：
In []: d1
Out[]: 
array([-45.50170186, -22.67585093, -15.03390062, ...,   4.90510204,
         4.95505051,   5.005     ])

In []: d2
Out[]: 
array([-45.60170186, -22.87585093, -15.33390062, ...,  -4.89489796,
        -4.94494949,  -4.995     ])

In []: result
Out[]: 
array([0.00000000e+000, 3.37791731e-116, 4.27087120e-053, ...,
       9.99999065e+001, 9.99999276e+001, 9.99999441e+001])"
"""

optionType = np.random.choice(('call','put'), len(combi))
ep = np.where(optionType == 'call', 1.0, -1.0)
       
result = (ep * S * si.norm.cdf(ep * d1, 0.0, 1.0) - ep * K * np.exp(-r * T) * si.norm.cdf(ep * d2, 0.0, 1.0))

"""
In []: optionType
Out[]: array(['call', 'put', 'call', ..., 'call', 'call', 'put'], dtype='<U4')

In []: ep
Out[]: array([ 1., -1.,  1., ...,  1.,  1., -1.])

"""