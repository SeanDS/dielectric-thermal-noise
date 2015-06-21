"""
Brownian noise in Advanced LIGO ETM
"""

from __future__ import division

import sys

sys.path.append('..')

import stacks
import matplotlib.pyplot as plt
import numpy as np

###
# Parameters

# wavelength
wavelength = 1064e-9 # [m]

# frequency range
f = np.logspace(1, 4, 1000) # [Hz]

# temperature
T = 290 # [K]

# beam sizes (distance from centre where power drops to 1/e)
wITM = 55e-3 # [m]
wETM = 62e-3 # [m]

###
# Calculation

stackITM = stacks.AdvancedLigoItmStack(wavelength)
stackETM = stacks.AdvancedLigoEtmStack(wavelength)

# calculate Brownian noise amplitude for frequency range
brownianNoiseITM = stackITM.brownianNoise(f, wITM, T)
brownianNoiseETM = stackETM.brownianNoise(f, wETM, T)

# combined noise for interferometer
brownianNoiseCombined = 2 * (brownianNoiseITM + brownianNoiseETM);

###
# Plot

# log-log plot
plt.loglog(f, np.sqrt(brownianNoiseITM), f, np.sqrt(brownianNoiseETM), f, np.sqrt(brownianNoiseCombined))

# axis labels, etc.
plt.legend(['ITM', 'ETM', 'Advanced LIGO Total'])
plt.xlabel('Frequency [Hz]')
plt.ylabel('Displacement-equivalent noise [m / sqrt(Hz)]')
plt.title('Brownian noise in Advanced LIGO ETM')

# add grid
plt.grid(True)

# display
plt.show()