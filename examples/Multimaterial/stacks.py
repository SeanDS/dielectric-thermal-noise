from __future__ import division

import sys

sys.path.append('../..')

import ditherm.materials as materials
import ditherm.layers as layers
import ditherm.stacks as stacks
import numpy as np

class SteinlechnerMultimaterialStack(stacks.Stack):
  """
  Dielectric stack as described in http://journals.aps.org/prd/abstract/10.1103/PhysRevD.91.042001.
  
  Poisson's ratio for amorphous silicon taken from http://www.mit.edu/~6.777/matprops/asi.htm
  """
  
  def __init__(self):    
    substrate = materials.Material("Silica Substrate", 7.2e10, 0.167, 5e-9, 1.45)
    coatingA = materials.Material("Silica Coating", 7.2e10, 0.17, 4e-5, 1.45)
    coatingB = materials.Material("Tantala Coating", 1.47e11, 0.23, 2.3e-4, 2.2)
    coatingC = materials.Material("Silicon Coating", 1.4e11, 0.22, 4.0e-4, 3.5)
    
    layerA = layers.Layer(coatingA, 267e-9)
    layerB = layers.Layer(coatingB, 176e-9)
    layerC = layers.Layer(coatingB, 111e-9)
    
    topLayer = layers.Layer(coatingA, 2*267e-9)

    theseLayers = np.array([topLayer, layerB] + [layerA, layerB] * 7 + [layerA, layerC] * 5)
    
    super(SteinlechnerMultimaterialStack, self).__init__(theseLayers, substrate)