% Script to extract calculated Brownian noise values from GWINC.
% Run from within the GWINC directory.

% load precomputed IFO model
load('ifo.mat');

% frequencies to calculate
f = logspace(-2, 5, 1000);

% calculate Brownian noise for mirrors
SbrITM  = getCoatBrownian(f, ifo, 'ITM');
SbrETM  = getCoatBrownian(f, ifo, 'ETM');

% save CSV file
csvwrite('aligo.csv', [f', SbrITM', SbrETM']);