# -*- coding: utf-8 -*-
"""
Created on Mon Nov 28 00:07:28 2022

@author: 53055
"""

from splearn.dataset.base import load_data_sample
from splearn.spectral import Spectral
from splearn.spectral import Hankle

def Hankle_Matrix(filename):
    train = load_data_sample(filename)
    
    est = Spectral()
    est.fit(train.data)
    lhankel = Hankel( sample_instance=pT.sample,
                     nbL=pT.nbL, nbEx=pT.nbEx, 
                     lrows=6, lcolumns=6, version="classic", 
                     partial=True, sparse=True, mode_quiet=True).lhankel
    return lhankel