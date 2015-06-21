from __future__ import division

import sys
import os

sys.path.append('..')

from unittest import TestCase

import materials
import layers
import stacks
import numpy as np

class AdvancedLigoEtmStack(stacks.Stack):
  def __init__(self, wavelength):
    substrate = materials.Material("Silica Substrate", 7.27e10, 0.167, 5e-9, 1.45)
    coatingA = materials.Material("Silica Coating", 7.2e10, 0.17, 4e-5, 1.45)
    coatingB = materials.Material("Titanium Tantala Coating", 1.4e11, 0.23, 2.3e-4, 2.06539)
    
    layerA = layers.Layer(coatingA, 0.27 * wavelength / coatingA.n)
    layerB = layers.Layer(coatingB, 0.23 * wavelength / coatingB.n)
    
    topLayer = layers.Layer(coatingA, 0.5 * wavelength / coatingA.n)
    baseLayer = layers.Layer(coatingA, 0.163870186147445 * wavelength / coatingB.n)

    theseLayers = np.array([topLayer, layerB] + [layerA, layerB] * 17 + [layerA, baseLayer])
    
    super(AdvancedLigoEtmStack, self).__init__(theseLayers, substrate)

class AdvancedLigoItmStack(stacks.Stack):
  def __init__(self, wavelength):
    substrate = materials.Material("Silica Substrate", 7.27e10, 0.167, 5e-9, 1.45)
    coatingA = materials.Material("Silica Coating", 7.2e10, 0.17, 4e-5, 1.45)
    coatingB = materials.Material("Titanium Tantala Coating", 1.4e11, 0.23, 2.3e-4, 2.06539)
    
    layerA = layers.Layer(coatingA, 0.308 * wavelength / coatingA.n)
    layerB = layers.Layer(coatingB, 0.192 * wavelength / coatingB.n)
    
    topLayer = layers.Layer(coatingA, 0.5 * wavelength / coatingA.n)
    baseLayer = layers.Layer(coatingA, 0.186957128029190 * wavelength / coatingB.n)

    theseLayers = np.array([topLayer, layerB] + [layerA, layerB] * 7 + [layerA, baseLayer])
    
    super(AdvancedLigoItmStack, self).__init__(theseLayers, substrate)

class TestBrownianNoise(TestCase):
  def setUp(self):
    self.etmStack = AdvancedLigoEtmStack(1064e-9)
    self.itmStack = AdvancedLigoItmStack(1064e-9)
  
  def test_d(self):
    self.assertAlmostEqual(self.etmStack.d(), 6.150299645767251e-6, delta=1e-20)
  
  def test_y_para(self):
    gwincVal = 9.651384066646355e10
    self.assertAlmostEqual(self.etmStack.yPara(), gwincVal, delta=0.3*gwincVal)
  
  def test_y_perp(self):
    gwincVal = 8.728318664479849e10
    self.assertAlmostEqual(self.etmStack.yPerp(), gwincVal, delta=0.3*gwincVal)
  
  def test_phi_para(self):
    gwincVal = 1.393560882693337e-4
    self.assertAlmostEqual(self.etmStack.phiPara(), gwincVal, delta=0.05*gwincVal)
  
  def test_phi_perp(self):
    gwincVal = 8.270302150752522e-5
    self.assertAlmostEqual(self.etmStack.phiPerp(), gwincVal, delta=0.05*gwincVal)
  
  def test_sigma_para(self):
    gwincVal = 0.2
    self.assertAlmostEqual(self.etmStack.sigmaPara(), gwincVal, delta=0.01*gwincVal)
  
  def test_sigma_perp(self):
    gwincVal = 0.201375606821895
    self.assertAlmostEqual(self.etmStack.sigmaPerp(), gwincVal, delta=0.01*gwincVal)

  def test_brownian_noise_itm(self):
    # load GWINC exported data
    gwincData = np.genfromtxt(os.path.join(os.path.dirname(__file__), 'gwinc', 'aligo.csv'), delimiter=',')
    
    wITM = 55e-3
    T = 290
    
    # calculate noise
    dithermITM = self.itmStack.brownianNoise(gwincData[:, 0], wITM, T)
    
    self.assertTrue(np.allclose(dithermITM, gwincData[:, 1], rtol=0.05, atol=0))
    
  def test_brownian_noise_etm(self):    
    # load GWINC exported data
    gwincData = np.genfromtxt(os.path.join(os.path.dirname(__file__), 'gwinc', 'aligo.csv'), delimiter=',')
    
    wETM = 62e-3
    T = 290
    
    # calculate noise
    dithermETM = self.etmStack.brownianNoise(gwincData[:, 0], wETM, T)
    
    self.assertTrue(np.allclose(dithermETM, gwincData[:, 2], rtol=0.05, atol=0))