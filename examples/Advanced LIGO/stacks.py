from __future__ import division

import sys

sys.path.append('../..')

import ditherm.materials as materials
import ditherm.layers as layers
import ditherm.stacks as stacks
import numpy as np

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