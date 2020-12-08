# -*- coding: utf-8 -*-
"""
Created on Sun Nov 22 21:08:04 2020

@author: franklin

https://aaronschlegel.me/black-scholes-formula-python.html
"""

import numpy as np
import scipy.stats as si
import itertools

def euro_vanilla(S, K, T, r, sigma, option = 'call'):
    
    #S: spot price
    #K: strike price
    #T: time to maturity
    #r: interest rate
    #sigma: volatility of underlying asset
    
    d1 = (np.log(S / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
    d2 = (np.log(S / K) + (r - 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
    
    if option == 'call':
        result = (S * si.norm.cdf(d1, 0.0, 1.0) - K * np.exp(-r * T) * si.norm.cdf(d2, 0.0, 1.0))
    if option == 'put': 
        result = (K * np.exp(-r * T) * si.norm.cdf(-d2, 0.0, 1.0) - S * si.norm.cdf(-d1, 0.0, 1.0))
        
    return result

S, K, T, r, sigma = (50, 100, 1, 0.05, 0.25)
retCall = euro_vanilla(S, K, T, r, sigma)
retPut = euro_vanilla(S, K, T, r, sigma, option = 'put')
print(retCall)
print(retPut)

arrayS = list(range(1,101))
arraySigma = [x * 0.1 for x in range(1,101)]

#直積
#A={a, b, c}, B={d, e}
#A×B={(a,d),(a,e),(b,d),(b,e),(c,d),(c,e)}A×B={(a,d),(a,e),(b,d),(b,e),(c,d),(c,e)}
combi = list(itertools.product(arrayS, arraySigma))

def calc():
    results = []
    for S, sigma in combi:
        pv = euro_vanilla(S, K, T, r, sigma)
        # print(pv)
        results.append(pv)
    return results

#%timeit calc()
PVs = calc()

# import numpy as np
# output=np.array(combi)
# np.savetxt('combi.csv', output, delimiter=',', fmt='%f')