# -*- coding: utf-8 -*-
"""
Created on Mon Nov 28 00:07:28 2022

@author: 53055
"""

from splearn.datasets.base import load_data_sample
from splearn.spectral import Spectral
from splearn.spectral import Hankel

def Hankel_Matrix(filename):
    train = load_data_sample(filename)
    
    est = Spectral()
    est.fit(train.data)
    lhankel = Hankel( sample_instance=train.data,
                     nbL=train.nbL, nbEx=train.nbEx, 
                     lrows=6, lcolumns=6, version="classic", 
                     partial=True, sparse=True, mode_quiet=True).lhankel
    return lhankel

if __name__ == "__main__":
    filename = "Test_store.json"
    lhankel = Hankel_Matrix(filename)   