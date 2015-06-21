from __future__ import division

class Material(object):
  def __init__(self, name, Y, sigma, phi, n):
    self.name = name
    self.Y = Y
    self.sigma = sigma
    self.phi = phi
    self.n = n
  
  @property
  def name(self):
    return self.__name
  
  @name.setter
  def name(self, name):
    self.__name = name
  
  @property
  def Y(self):
    return self.__Y
  
  @Y.setter
  def Y(self, Y):
    self.__Y = Y
  
  @property
  def sigma(self):
    return self.__sigma
  
  @sigma.setter
  def sigma(self, sigma):
    self.__sigma = sigma

  @property
  def phi(self):
    return self.__phi
  
  @phi.setter
  def phi(self, phi):
    self.__phi = phi
  
  @property
  def n(self):
    return self.__n
  
  @n.setter
  def n(self, n):
    self.__n = n

class SilicaCoating(Material):
  def __init__(self, *args, **kwargs):
    super(SilicaCoating, self).__init__("Silica", 72e9, 0.17, 4e-5, 1.45)

class TantalaCoating(Material):
  def __init__(self, *args, **kwargs):
    super(TantalaCoating, self).__init__("Tantala", 140e9, 0.23, 3.8e-4, 2.06)

class TitaniumTantalaCoating(Material):
  def __init__(self, *args, **kwargs):
    super(TitaniumTantalaCoating, self).__init__("Titanium doped Tantala", 140e9, 0.23, 3e-4, 2.06)

class SilicaSubstrate(Material):
  def __init__(self, *args, **kwargs):
    super(SilicaSubstrate, self).__init__("Silica", 72e9, 0.17, 5e-9, 1.45)  