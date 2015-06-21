# Ditherm: Dielectric Thermal Noise Calculator
This is a tool to calculate Brownian thermal noise in dielectric mirror stacks.

It supports noise calculations for n-layer stacks of any material, but it has only been tested in the following scenarios:
 - Two-material stacks using data from the [Advanced LIGO](https://www.advancedligo.mit.edu/) noise calculator, [GWINC](https://awiki.ligo-wa.caltech.edu/aLIGO/GWINC) (link requires albert.einstein style credentials, available to members of the LIGO Scientific Community only)
 - A three-material stack using a single data point from [Steinlechner et al.](http://journals.aps.org/prd/abstract/10.1103/PhysRevD.91.042001)

The code can calculate arbitrary material stacks due to an extension to a two-material Brownian thermal noise calculation provided in scientific literature. The extension is unpublished and probably wrong, but this is hopefully the beginning of something that will one day produce trusted results. Due to the lack of systematic testing, take what this script says with a heavy pinch of salt - you have been warned!

## More Notes ##
I provide this software without any kind of guarantee that it provides the correct answer. This software is in no way affiliated with or endorsed by any university or organisation - it is purely the work of a private individual.

In particular, the extension from the two-material Brownian noise calculation (mostly based on Harry et al., 2002) to an n-material calculation was performed simply by inspecting the formulae. I don't know if this is reasonable or not. I suspect that for coatings with more than a few (~3) materials and with extremely small or large (outwith the range wavelength * 0.15 to wavelength * 0.35) optical thicknesses per layer, the results will diverge from reality. Use at your own risk!

## Testing ##
To test the software against precomputed values from GWINC, run:

`python ditherm test`

from the root Ditherm directory (the same directory as this readme).

## Future Work ##
 - Implement phase correction to Brownian calculation as per the functions on [this page](https://awiki.ligo-wa.caltech.edu/aLIGO/GWINC)
 - Look at proper way to combine multiple materials by reading these papers:
   - http://journals.aps.org/prd/abstract/10.1103/PhysRevD.91.042002
   - http://journals.aps.org/prd/abstract/10.1103/PhysRevD.87.082001
   - http://journals.aps.org/prd/abstract/10.1103/PhysRevD.91.042001

## Credits ##
This implementation was written by Sean Leavey, but the calculations are based on a number of sources:
 - http://dx.doi.org/10.1088/0264-9381/19/5/305
 - http://proceedings.spiedigitallibrary.org/proceeding.aspx?articleid=851432 (for the correction to perpendicular component of the loss angle from Harry et al. 2002)
 - http://dx.doi.org/10.1088/0264-9381/24/2/008
 - GWINC (for the simplified version of the parallel component of Poisson's ratio)
 - Personal discussion with colleagues
 
Sean Leavey  
https://github.com/SeanDS/