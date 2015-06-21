"""
Brownian noise in multimaterial stack described in Phys. Rev. D 91, 042001
(http://journals.aps.org/prd/abstract/10.1103/PhysRevD.91.042001)

Beam size assumed to be that of ET-HF (see p242 of https://tds.ego-gw.it/itf/tds/index.php?callContent=2&callCode=8709)
"""

from __future__ import division

import sys

sys.path.append('..')

import stacks
import matplotlib.pyplot as plt
import numpy as np

###
# Parameters

# frequency range
f = np.logspace(0, 3, 1000) # [Hz]

# temperature
T = 290 # [K]

# beam sizes (distance from centre where power drops to 1/e)
w = 72.5e-3 # [m]

###
# Calculation

stack = stacks.SteinlechnerMultimaterialStack()

# calculate Brownian noise amplitude for frequency range
brownianNoise = stack.brownianNoise(f, w, T)

###
# Plot

# log-log plot
plt.loglog(f, np.sqrt(brownianNoise))

# axis labels, etc.
plt.xlabel('Frequency [Hz]')
plt.ylabel('Displacement-equivalent noise [m / sqrt(Hz)]')
plt.title('Brownian noise in multilayer coating from Phys. Rev. D 91, 042001')

# add grid
plt.grid(True)

# display
plt.show()