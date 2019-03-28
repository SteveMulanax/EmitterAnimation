#!/usr/bin/env python
#
# randy.py
#
# By Steve Mulanax 2/28/2019

import numpy as np
import matplotlib.pyplot as plt

"""
Plot the set of 'shaped' random numbers for particle brightness level deltas

:param bd_mean: Average fade (negative) or boost (positive) per particle
    per step. The default value is computed (-2 * 256 / _size) if the
    field is not set.
:param bd_mu: Average distance from mean for the positive and negative
    variations.
:param bd_sigma: Standard deviation from mu for variations on the
    positive and negative sides. The default value is computed (mu *
    0.25) if the field is not set.
"""
bd_mean = -32
bd_mu = 32
bd_sigma = bd_mu * 0.25

bd1 = np.random.normal(bd_mean - bd_mu, bd_sigma, 16).astype(int)
bd2 = np.random.normal(bd_mean + bd_mu, bd_sigma, 16).astype(int)
bd = np.concatenate((bd1, bd2), axis=0)

count, bins, ignored = plt.hist(bd, bins=100, density=True)

label_y = max(count) * 0.95

plt.plot(
    bins,
    1/(bd_sigma * np.sqrt(2*np.pi)) *
    np.exp(-(bins-(bd_mu+bd_mean))**2 / (2*bd_sigma**2)),
    linewidth=4,
    color='g')
plt.axvline(bd_mean+bd_mu, ls='--', color='g')
plt.text(
    bd_mean+bd_mu, label_y,
    'bd_mean+bd_mu={}'.format(bd_mean+bd_mu),
    color='g',
    rotation=90)
plt.axvline(bd_mean+bd_mu+bd_sigma, ls='--', color='g')
plt.text(
    bd_mean+bd_mu+bd_sigma, label_y,
    'bd_mean+bd_mu+bd_sigma={}'.format(bd_mean+bd_mu+bd_sigma),
    color='g',
    rotation=90)
plt.axvline(bd_mean+bd_mu-bd_sigma, ls='--', color='g')
plt.text(
    bd_mean+bd_mu-bd_sigma, label_y,
    'bd_mean+bd_mu-bd_sigma={}'.format(bd_mean+bd_mu-bd_sigma),
    color='g',
    rotation=90)

plt.plot(
    bins,
    1/(bd_sigma * np.sqrt(2*np.pi)) *
    np.exp(-(bins-(bd_mean-bd_mu))**2 / (2*bd_sigma**2)),
    linewidth=4,
    color='r')
plt.axvline(bd_mean-bd_mu, ls='--', color='r')
plt.text(
    bd_mean-bd_mu, label_y,
    'bd_mean-bd_mu={}'.format(bd_mean-bd_mu),
    color='r',
    rotation=90)
plt.axvline(bd_mean-bd_mu+bd_sigma, ls='--', color='r')
plt.text(
    bd_mean-bd_mu+bd_sigma, label_y,
    'bd_mean-bd_mu+bd_sigma={}'.format(bd_mean-bd_mu+bd_sigma),
    color='r',
    rotation=90)
plt.axvline(bd_mean-bd_mu-bd_sigma, ls='--', color='r')
plt.text(
    bd_mean-bd_mu-bd_sigma, label_y,
    'bd_mean-bd_mu-bd_sigma={}'.format(bd_mean-bd_mu-bd_sigma),
    color='r',
    rotation=90)

plt.axvline(bd_mean, ls='--')
plt.text(bd_mean, label_y, 'bd_mean={}'.format(bd_mean), rotation=90)

plt.title('Histogram of Random Brightness-Level Changes')
plt.ylabel('Bin Count')
plt.xlabel('Brightness Delta')

plt.show()
