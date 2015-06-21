from __future__ import division

import numpy as np

import layers
import materials

class Stack(object):
  def __init__(self, layers, substrate):
    self.layers = layers
    self.substrate = substrate

  @property
  def layers(self):
    return self.__layers
  
  @layers.setter
  def layers(self, layers):
    self.__layers = layers
  
  @property
  def substrate(self):
    return self.__substrate
  
  @substrate.setter
  def substrate(self, substrate):
    self.__substrate = substrate
  
  def d(self):
    """
    Total thickness.
    """
    
    return sum(layer.d for layer in self.layers)
    
  def yPara(self):
    """
    Total parallel Young's modulus.
    """
    
    return 1 / self.d() * sum([layer.d * layer.material.Y for layer in self.layers])
    
  def yPerp(self):
    """
    Total perpendicular Young's modulus.
    """
    
    return self.d() / sum([layer.d / layer.material.Y for layer in self.layers])
  
  def phiPara(self):    
    """
    Total parallel loss angle.
    """
    
    return 1 / (self.d() * self.yPara()) * sum([layer.material.Y * layer.material.phi * layer.d for layer in self.layers])
    
  def phiPerp(self):
    """
    Total perpendicular loss angle.
    """
    
    return self.yPerp() / self.d() * sum([layer.d * layer.material.phi / layer.material.Y for layer in self.layers])
    
  def sigmaPara(self):
    """
    Total stack parallel Poisson ratio.
    """
    
    return np.mean([layer.material.sigma for layer in self.layers])
    
  def sigmaPerp(self):
    """
    Total perpendicular Poisson ratio.
    """
    
    return sum([layer.material.sigma * layer.material.Y * layer.d for layer in self.layers]) / sum([layer.material.Y * layer.d for layer in self.layers])
    
  def phi(self, beamSize):
    """
    Effective loss angle.
    """
    
    return (self.d() / (np.sqrt(np.pi) * beamSize * self.yPerp()) *
            (self.phiPerp() *
             (self.substrate.Y / (1 - self.substrate.sigma ** 2) -
              2 * self.sigmaPerp() ** 2 * self.substrate.Y * self.yPara() /
              (self.yPerp() * (1 - self.substrate.sigma ** 2) * (1 - self.sigmaPara()))) +
             self.yPara() * self.sigmaPerp() * (1 - 2 * self.substrate.sigma) /
             ((1 - self.sigmaPara()) * (1 - self.substrate.sigma)) *
             (self.phiPara() - self.phiPerp()) +
             self.yPara() * self.yPerp() * (1 + self.substrate.sigma) *
             (self.phiPara() * (1 - 2 * self.substrate.sigma) ** 2) /
             (self.substrate.Y * (1 - self.sigmaPara() ** 2) * (1 - self.substrate.sigma))))

  def brownianNoise(self, freq, beamSize, temperature):
    k = 1.3806503e-23;
    
    return 2 * k * temperature / (np.sqrt(np.pi ** 3) * freq * beamSize * self.substrate.Y) * (1 - self.substrate.sigma ** 2) * self.phi(beamSize)
  
    # GWINC version, which does the same thing
    #c = self.d()*(1-self.substrate.sigma**2)/(np.pi*beamSize**2)*((1/(self.yPerp()*(1-self.substrate.sigma**2))-2*self.sigmaPerp()**2*self.yPara()/(self.yPerp()**2*(1-self.substrate.sigma**2)*(1-self.sigmaPara())))*self.phiPerp() + self.yPara()*self.sigmaPerp()*(1-2*self.substrate.sigma)/(self.yPerp()*self.substrate.Y*(1-self.sigmaPara())*(1-self.substrate.sigma))*(self.phiPara()-self.phiPerp())+self.yPara()*(1+self.substrate.sigma)*(1-2*self.substrate.sigma)**2/(self.substrate.Y**2*(1-self.sigmaPara()**2)*(1-self.substrate.sigma))*self.phiPara())
    #return 4 * k * temperature * c / (2 * np.pi * freq)