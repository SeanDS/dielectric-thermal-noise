from __future__ import division

import materials

class Layer(object):
  def __init__(self, material, d):
    self.material = material
    self.d = d
  
  @property
  def material(self):
    return self.__material

  @material.setter
  def material(self, material):
    self.__material = material
  
  @property
  def d(self):
    """
    Layer physical thickness.
    """
    
    return self.__d
  
  @d.setter
  def d(self, d):
    self.__d = d

class Bilayer(object):
  def __init__(self, layerA, layerB):
    self.layerA = layerA
    self.layerB = layerB
  
  @property
  def layerA(self):
    return self.__layerA
  
  @layerA.setter
  def layerA(self, layerA):
    self.__layerA = layerA

  @property
  def layerB(self):
    return self.__layerB
  
  @layerB.setter
  def layerB(self, layerB):
    self.__layerB = layerB
    
  def d(self):
    """
    Total bilayer physical thickness.
    """
    
    return self.layerA.d + self.layerB.d
    
  def yPara(self):
    """
    Parallel component of Young's modulus.
    """
    
    return 1 / self.d() * (self.layerA.d * self.layerA.material.Y + self.layerB.d * self.layerB.material.Y)
  
  def yPerp(self):
    """
    Perpendicular component of Young's modulus.
    """
    
    return self.d() / (self.layerA.d / self.layerA.material.Y + self.layerB.d / self.layerB.material.Y)
    
  def phiPara(self):
    """
    Parallel component of loss angle.
    """
    
    return 1 / (self.d() * self.yPara()) * (self.layerA.material.Y * self.layerA.material.phi * self.layerA.d + self.layerB.material.Y * self.layerB.material.phi * self.layerB.d)
    
  def phiPerp(self):
    """
    Perpendicular component of loss angle.
    """
    
    return self.yPerp() / self.d() * (self.layerA.d * self.layerA.material.phi / self.layerA.material.Y + self.layerB.d * self.layerB.material.phi / self.layerB.material.Y)

  def sigmaPara(self):
    """
    Parallel component of Poisson ratio.
    """
    
    return (self.layerA.d * self.layerA.material.sigma * self.layerA.material.Y * (1 - self.layerA.material.sigma ** 2) + self.layerB.d * self.layerB.material.sigma * self.layerB.material.Y * (1 - self.layerB.material.sigma ** 2)) / (self.layerA.d * self.layerA.material.Y * (1 - self.layerB.material.sigma ** 2) + self.layerB.d * self.layerB.material.Y * (1 - self.layerA.material.sigma ** 2))

  def sigmaPerp(self):
    """
    Perpendicular component of Poisson ratio.
    """
    
    return (self.layerA.material.sigma * self.layerA.material.Y * self.layerA.d + self.layerB.material.sigma * self.layerB.material.Y * self.layerB.d) / (self.layerA.material.Y * self.layerA.d + self.layerB.material.Y * self.layerB.d)