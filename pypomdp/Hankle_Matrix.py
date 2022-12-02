# -*- coding: utf-8 -*-
"""
Created on Mon Nov 28 00:07:28 2022

@author: 53055
"""

from splearn.datasets.base import load_data_sample
from splearn.spectral import Spectral
from splearn  import Hankel
from splearn.automaton import Automaton

def Hankel_Matrix(filename):
    train = load_data_sample(filename)
    
    est = Spectral()
    est.set_params(lrows = 3, lcolumns = 3, smooth_method = 'trigram', version = 'factor', rank = 8)
    est.fit(train.data)
    # print(est.automaton.transitions)
    # print(train.fact)
    lhankel = Hankel( sample_instance=None, 
                      lrows=6, lcolumns=6, version="classic", 
                      partial=True, sparse=True, mode_quiet=True).lhankel
    return train
    return lhankel

if __name__ == "__main__":
    filename = "Test_store.json"
    auto = Automaton.SimpleExample()
    print(auto.transitions)
    lhankel = Hankel_Matrix(filename)   